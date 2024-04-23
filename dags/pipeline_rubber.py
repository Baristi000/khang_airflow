import pandas as pd
import numpy as np
import requests
import time
import random
import pandas as pd
import json
import pendulum
from dags.create_table import *
from dags.SourceToStage import *
# import dags.create_table as qr
from airflow import DAG
from airflow.operators.python import PythonOperator
# from airflow.models.connection import Connection
from airflow.providers.postgres.operators.postgres import PostgresOperator


default_args = {
    'start_date': pendulum.datetime(2024,4,21,tz='UTC'),
    'owner': 'airflow'
}
dag = DAG('pipeline_rubber', default_args=default_args,schedule_interval='@once',catchup=False)

create_written_table = PostgresOperator(
    task_id='create_table_Country',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Country,
    dag=dag
)
StageToNDS_Country = PostgresOperator(
    task_id='StageToNDS_Country',
    sql= ''' 
        MERGE INTO "NDS".country AS t1
        USING "Stage".country AS t2
        ON (t1.CountryID = t2.CountryID)
        WHEN MATCHED THEN
            UPDATE SET
                CountryName = t2.CountryName,
                UpdateDate = t2.UpdateDate
        WHEN NOT MATCHED THEN
            INSERT (CountryID, CountryName, CreatedDate, UpdateDate)
            VALUES (t2.CountryID, t2.CountryName, t2.CreatedDate, t2.UpdateDate);   
    ''',
    postgres_conn_id='pg_connection_1',
)
create_written_table >> StageToNDS_Country
# create_table_Region = PostgresOperator(
#     task_id='create_table_Region',
#     postgres_conn_id='pg_connection_1',
#     sql=create_table_Region,
#     dag=dag
# )
# create_table_Address = PostgresOperator(
#     task_id='create_table_Address',
#     postgres_conn_id='pg_connection_1',
#     sql=create_table_Address,
#     dag=dag
# )
# create_table_Account = PostgresOperator(
#     task_id='create_table_Account',
#     postgres_conn_id='pg_connection_1',
#     sql=create_table_Account,
#     dag=dag
# )

# create_table_UserInfo = PostgresOperator(
#     task_id='create_table_UserInfo',
#     postgres_conn_id='pg_connection_1',
#     sql=create_table_UserInfo,
#     dag=dag
# )
# create_table_Field = PostgresOperator(
#     task_id='create_table_Field',
#     postgres_conn_id='pg_connection_1',
#     sql=create_table_Field,
#     dag=dag
# )
# create_table_RubberTree = PostgresOperator(
#     task_id='create_table_RubberTree',
#     postgres_conn_id='pg_connection_1',
#     sql=create_table_RubberTree,
#     dag=dag
# )
# create_table_RubberTreeInformation = PostgresOperator(
#     task_id='create_table_RubberTreeInformation',
#     postgres_conn_id='pg_connection_1',
#     sql=create_table_RubberTreeInformation,
#     dag=dag
# )
# create_table_Plan = PostgresOperator(
#     task_id='create_table_Plan',
#     postgres_conn_id='pg_connection_1',
#     sql=create_table_Plan,
#     dag=dag
# )
# create_table_PlanDetail = PostgresOperator(
#     task_id='create_table_PlanDetail',
#     postgres_conn_id='pg_connection_1',
#     sql=create_table_PlanDetail,
#     dag=dag
# )
# create_table_Lidar = PostgresOperator(
#     task_id='create_table_Lidar',
#     postgres_conn_id='pg_connection_1',
#     sql=create_table_Lidar,
#     dag=dag
# )
# create_table_Camera = PostgresOperator(
#     task_id='create_table_Camera',
#     postgres_conn_id='pg_connection_1',
#     sql=create_table_Camera,
#     dag=dag
# )
# create_table_Radar = PostgresOperator(
#     task_id='create_table_Radar',
#     postgres_conn_id='pg_connection_1',
#     sql=create_table_Radar,
#     dag=dag
# )
# create_table_SensorControlSystem = PostgresOperator(
#     task_id='create_table_SensorControlSystem',
#     postgres_conn_id='pg_connection_1',
#     sql=create_table_SensorControlSystem,
#     dag=dag
# )
# create_table_Robot = PostgresOperator(  
#     task_id='create_table_Robot',
#     postgres_conn_id='pg_connection_1',
#     sql=create_table_Robot,
#     dag=dag
# )
# create_table_Energy = PostgresOperator(
#     task_id='create_table_Energy',
#     postgres_conn_id='pg_connection_1',
#     sql=create_table_Energy,
#     dag=dag
# )
# create_table_RobotTapping = PostgresOperator(
#     task_id='create_table_RobotTapping',
#     postgres_conn_id='pg_connection_1',
#     sql=create_table_RobotTapping,
#     dag=dag
# )
# create_table_Blade = PostgresOperator(
#     task_id='create_table_Blade',
#     postgres_conn_id='pg_connection_1',
#     sql=create_table_Blade,
#     dag=dag
# )
# create_table_Environment = PostgresOperator(
#     task_id='create_table_Environment',
#     postgres_conn_id='pg_connection_1',
#     sql=create_table_Environment,
#     dag=dag
# )
# create_table_Drone = PostgresOperator(
#     task_id='create_table_Drone',
#     postgres_conn_id='pg_connection_1',
#     sql=create_table_Drone,
#     dag=dag
# )
# create_table_DroneInformation = PostgresOperator(
#     task_id='create_table_DroneInformation',
#     postgres_conn_id='pg_connection_1',
#     sql=create_table_DroneInformation,
#     dag=dag
# )
# create_table_DroneImage = PostgresOperator(
#     task_id='create_table_DroneImage',
#     postgres_conn_id='pg_connection_1',
#     sql=create_table_DroneImage,
#     dag=dag
# )
# create_table_ChargingStation = PostgresOperator(
#     task_id='create_table_ChargingStation',
#     postgres_conn_id='pg_connection_1',
#     sql=create_table_ChargingStation,
#     dag=dag
# )
# create_table_ChargingStatus = PostgresOperator(
#     task_id='create_table_ChargingStatus',
#     postgres_conn_id='pg_connection_1',
#     sql=create_table_ChargingStatus,
#     dag=dag
# )
# create_table_Task = PostgresOperator(
#     task_id='create_table_Task',
#     postgres_conn_id='pg_connection_1',
#     sql=create_table_Task,
#     dag=dag
# )
# insert_Country = PostgresOperator(
#     task_id='insert_Country',
#     sql='INSERT INTO "NDS".Country SELECT * FROM "Stage".Country',
#     postgres_conn_id='pg_connection_1',
# )
# insert_account = PostgresOperator(
#     task_id='insert_account',
#     sql='INSERT INTO "NDS".account SELECT * FROM "Stage".account',
#     postgres_conn_id='pg_connection_1',
# )

# truncateTableAndSetCet_Country = PostgresOperator(
#     task_id='truncateTableAndSetCet_Country',
#     sql= truncateTableAndSetCet_Country,
#     postgres_conn_id='pg_connection_1',
# )
# sourceToStage_Country = PostgresOperator(
#     task_id='sourceToStage_Country',
#     sql= sourceToStage_Country,
#     postgres_conn_id='pg_connection_1',
# )
# setLset_Country = PostgresOperator(
#     task_id='setLset_Country',
#     sql = setLset_Country,
#     postgres_conn_id='pg_connection_1',
# )

# truncateTableAndSetCet_Region = PostgresOperator(
#     task_id='truncateTableAndSetCet_Region',
#     sql= truncateTableAndSetCet_Region,
#     postgres_conn_id='pg_connection_1',
# )
# sourceToStage_Region = PostgresOperator(
#     task_id='sourceToStage_Region',
#     sql= sourceToStage_Region,
#     postgres_conn_id='pg_connection_1',
# )
# setLset_Region = PostgresOperator(
#     task_id='setLset_Region',
#     sql = setLset_Region,
#     postgres_conn_id='pg_connection_1',
# )

# truncateTableAndSetCet_Address = PostgresOperator(
#     task_id='truncateTableAndSetCet_Address',
#     sql= truncateTableAndSetCet_Address,
#     postgres_conn_id='pg_connection_1',
# )
# sourceToStage_Address = PostgresOperator(
#     task_id='sourceToStage_Address',
#     sql= sourceToStage_Address,
#     postgres_conn_id='pg_connection_1',
# )
# setLset_Address = PostgresOperator(
#     task_id='setLset_Address',
#     sql = setLset_Address,
#     postgres_conn_id='pg_connection_1',
# )

# truncateTableAndSetCet_country >> sourceToStage_country >> setLset_country
# create_written_table >> truncateTableAndSetCet_Region >> sourceToStage_Region >> setLset_Region

# create_written_table >>create_table_Region>>create_table_Address
# create_table_Address>>create_table_Account>>create_table_UserInfo>>create_table_Field>>create_table_RubberTree>>create_table_RubberTreeInformation
# create_table_RubberTreeInformation>>create_table_Plan>>create_table_PlanDetail>>create_table_Lidar>>create_table_Camera>>create_table_Radar>>create_table_SensorControlSystem
# create_table_SensorControlSystem>> create_table_Robot>>create_table_Energy>>create_table_RobotTapping>>create_table_Blade>>create_table_Environment>>create_table_Drone
# create_table_Drone>> create_table_DroneInformation>>create_table_DroneImage>>create_table_ChargingStation>>create_table_ChargingStatus>>create_table_Task >> insert_account

