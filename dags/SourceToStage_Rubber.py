import pandas as pd
import numpy as np
import requests
import time
import random
import pandas as pd
import json
import pendulum
from dags.sql.SourceToStage import *
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
    'start_date': pendulum.datetime(2024,4,24,tz='UTC'),
    'owner': 'airflow1'
}
dag = DAG('SourceToStage_Rubber', default_args=default_args,schedule_interval='@once',catchup=False)


truncateTableAndSetCet_Country = PostgresOperator(
    task_id='truncateTableAndSetCet_Country',
    sql= truncateTableAndSetCet_Country,
    postgres_conn_id='pg_connection_1',
    dag=dag
) 
sourceToStage_Country = PostgresOperator(
    task_id='sourceToStage_Country',
    sql= sourceToStage_Country,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
setLset_Country = PostgresOperator(
    task_id='setLset_Country',
    sql = setLset_Country,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
# truncateTableAndSetCet_Country >> sourceToStage_Country >> setLset_Country

truncateTableAndSetCet_Region = PostgresOperator(
    task_id='truncateTableAndSetCet_Region',
    sql= truncateTableAndSetCet_Region,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
sourceToStage_Region = PostgresOperator(
    task_id='sourceToStage_Region',
    sql= sourceToStage_Region,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
setLset_Region = PostgresOperator(
    task_id='setLset_Region',
    sql = setLset_Region,
    postgres_conn_id='pg_connection_1',
    dag=dag
)

truncateTableAndSetCet_Address = PostgresOperator(
    task_id='truncateTableAndSetCet_Address',
    sql= truncateTableAndSetCet_Address,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
sourceToStage_Address = PostgresOperator(
    task_id='sourceToStage_Address',
    sql= sourceToStage_Address,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
setLset_Address = PostgresOperator(
    task_id='setLset_Address',
    sql = setLset_Address,
    postgres_conn_id='pg_connection_1',
    dag=dag
)

truncateTableAndSetCet_Account = PostgresOperator(
    task_id='truncateTableAndSetCet_Account',
    sql= truncateTableAndSetCet_Account,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
sourceToStage_Account = PostgresOperator(
    task_id='sourceToStage_Account',
    sql= sourceToStage_Account,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
setLset_Account = PostgresOperator(
    task_id='setLset_Account',
    sql = setLset_Account,
    postgres_conn_id='pg_connection_1',
    dag=dag
)

truncateTableAndSetCet_UserInfo = PostgresOperator(
    task_id='truncateTableAndSetCet_UserInfo',
    sql= truncateTableAndSetCet_UserInfo,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
sourceToStage_UserInfo = PostgresOperator(
    task_id='sourceToStage_UserInfo',
    sql= sourceToStage_UserInfo,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
setLset_UserInfo = PostgresOperator(
    task_id='setLset_UserInfo',
    sql = setLset_UserInfo,
    postgres_conn_id='pg_connection_1',
    dag=dag
)

truncateTableAndSetCet_Field = PostgresOperator(
    task_id='truncateTableAndSetCet_Field',
    sql= truncateTableAndSetCet_Field,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
sourceToStage_Field = PostgresOperator(
    task_id='sourceToStage_Field',
    sql= sourceToStage_Field,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
setLset_Field = PostgresOperator(
    task_id='setLset_Field',
    sql = setLset_Field,
    postgres_conn_id='pg_connection_1',
    dag=dag
)

truncateTableAndSetCet_RubberTree = PostgresOperator(
    task_id='truncateTableAndSetCet_RubberTree',
    sql= truncateTableAndSetCet_RubberTree,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
sourceToStage_RubberTree = PostgresOperator(
    task_id='sourceToStage_RubberTree',
    sql= sourceToStage_RubberTree,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
setLset_RubberTree = PostgresOperator(
    task_id='setLset_RubberTree',
    sql = setLset_RubberTree,
    postgres_conn_id='pg_connection_1',
    dag=dag
)

truncateTableAndSetCet_RubberTreeInformation = PostgresOperator(
    task_id='truncateTableAndSetCet_RubberTreeInformation',
    sql= truncateTableAndSetCet_RubberTreeInformation,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
sourceToStage_RubberTreeInformation = PostgresOperator(
    task_id='sourceToStage_RubberTreeInformation',
    sql= sourceToStage_RubberTreeInformation,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
setLset_RubberTreeInformation = PostgresOperator(
    task_id='setLset_RubberTreeInformation',
    sql = setLset_RubberTreeInformation,
    postgres_conn_id='pg_connection_1',
    dag=dag
)

truncateTableAndSetCet_Plan = PostgresOperator(
    task_id='truncateTableAndSetCet_Plan',
    sql= truncateTableAndSetCet_Plan,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
sourceToStage_Plan = PostgresOperator(
    task_id='sourceToStage_Plan',
    sql= sourceToStage_Plan,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
setLset_Plan = PostgresOperator(
    task_id='setLset_Plan',
    sql = setLset_Plan,
    postgres_conn_id='pg_connection_1',
    dag=dag
)

truncateTableAndSetCet_PlanDetail = PostgresOperator(
    task_id='truncateTableAndSetCet_PlanDetail',
    sql= truncateTableAndSetCet_PlanDetail,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
sourceToStage_PlanDetail = PostgresOperator(
    task_id='sourceToStage_PlanDetail',
    sql= sourceToStage_PlanDetail,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
setLset_PlanDetail = PostgresOperator(
    task_id='setLset_PlanDetail',
    sql = setLset_PlanDetail,
    postgres_conn_id='pg_connection_1',
    dag=dag
)

truncateTableAndSetCet_Lidar = PostgresOperator(
    task_id='truncateTableAndSetCet_Lidar',
    sql= truncateTableAndSetCet_Lidar,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
sourceToStage_Lidar = PostgresOperator(
    task_id='sourceToStage_Lidar',
    sql= sourceToStage_Lidar,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
setLset_Lidar = PostgresOperator(
    task_id='setLset_Lidar',
    sql = setLset_Lidar,
    postgres_conn_id='pg_connection_1',
    dag=dag
)

truncateTableAndSetCet_Camera = PostgresOperator(
    task_id='truncateTableAndSetCet_Camera',
    sql= truncateTableAndSetCet_Camera,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
sourceToStage_Camera = PostgresOperator(
    task_id='sourceToStage_Camera',
    sql= sourceToStage_Camera,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
setLset_Camera = PostgresOperator(
    task_id='setLset_Camera',
    sql = setLset_Camera,
    postgres_conn_id='pg_connection_1',
    dag=dag
)

truncateTableAndSetCet_Radar = PostgresOperator(
    task_id='truncateTableAndSetCet_Radar',
    sql= truncateTableAndSetCet_Radar,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
sourceToStage_Radar = PostgresOperator(
    task_id='sourceToStage_Radar',
    sql= sourceToStage_Radar,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
setLset_Radar = PostgresOperator(
    task_id='setLset_Radar',
    sql = setLset_Radar,
    postgres_conn_id='pg_connection_1',
    dag=dag
)

truncateTableAndSetCet_SensorControlSystem = PostgresOperator(
    task_id='truncateTableAndSetCet_SensorControlSystem',
    sql= truncateTableAndSetCet_SensorControlSystem,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
sourceToStage_SensorControlSystem = PostgresOperator(
    task_id='sourceToStage_SensorControlSystem',
    sql= sourceToStage_SensorControlSystem,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
setLset_SensorControlSystem = PostgresOperator(
    task_id='setLset_SensorControlSystem',
    sql = setLset_SensorControlSystem,
    postgres_conn_id='pg_connection_1',
    dag=dag
)

truncateTableAndSetCet_Robot = PostgresOperator(
    task_id='truncateTableAndSetCet_Robot',
    sql= truncateTableAndSetCet_Robot,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
sourceToStage_Robot = PostgresOperator(
    task_id='sourceToStage_Robot',
    sql= sourceToStage_Robot,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
setLset_Robot = PostgresOperator(
    task_id='setLset_Robot',
    sql = setLset_Robot,
    postgres_conn_id='pg_connection_1',
    dag=dag
)

truncateTableAndSetCet_Energy = PostgresOperator(
    task_id='truncateTableAndSetCet_Energy',
    sql= truncateTableAndSetCet_Energy,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
sourceToStage_Energy = PostgresOperator(
    task_id='sourceToStage_Energy',
    sql= sourceToStage_Energy,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
setLset_Energy = PostgresOperator(
    task_id='setLset_Energy',
    sql = setLset_Energy,
    postgres_conn_id='pg_connection_1',
    dag=dag
)

truncateTableAndSetCet_RobotTapping = PostgresOperator(
    task_id='truncateTableAndSetCet_RobotTapping',
    sql= truncateTableAndSetCet_RobotTapping,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
sourceToStage_RobotTapping = PostgresOperator(
    task_id='sourceToStage_RobotTapping',
    sql= sourceToStage_RobotTapping,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
setLset_RobotTapping = PostgresOperator(
    task_id='setLset_RobotTapping',
    sql = setLset_RobotTapping,
    postgres_conn_id='pg_connection_1',
    dag=dag
)

truncateTableAndSetCet_Blade = PostgresOperator(
    task_id='truncateTableAndSetCet_Blade',
    sql= truncateTableAndSetCet_Blade,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
sourceToStage_Blade = PostgresOperator(
    task_id='sourceToStage_Blade',
    sql= sourceToStage_Blade,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
setLset_Blade = PostgresOperator(
    task_id='setLset_Blade',
    sql = setLset_Blade,
    postgres_conn_id='pg_connection_1',
    dag=dag
)

truncateTableAndSetCet_Environment = PostgresOperator(
    task_id='truncateTableAndSetCet_Environment',
    sql= truncateTableAndSetCet_Environment,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
sourceToStage_Environment = PostgresOperator(
    task_id='sourceToStage_Environment',
    sql= sourceToStage_Environment,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
setLset_Environment = PostgresOperator(
    task_id='setLset_Environment',
    sql = setLset_Environment,
    postgres_conn_id='pg_connection_1',
    dag=dag
)

truncateTableAndSetCet_Drone = PostgresOperator(
    task_id='truncateTableAndSetCet_Drone',
    sql= truncateTableAndSetCet_Drone,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
sourceToStage_Drone = PostgresOperator(
    task_id='sourceToStage_Drone',
    sql= sourceToStage_Drone,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
setLset_Drone = PostgresOperator(
    task_id='setLset_Drone',
    sql = setLset_Drone,
    postgres_conn_id='pg_connection_1',
    dag=dag
)

truncateTableAndSetCet_DroneInformation = PostgresOperator(
    task_id='truncateTableAndSetCet_DroneInformation',
    sql= truncateTableAndSetCet_DroneInformation,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
sourceToStage_DroneInformation = PostgresOperator(
    task_id='sourceToStage_DroneInformation',
    sql= sourceToStage_DroneInformation,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
setLset_DroneInformation = PostgresOperator(
    task_id='setLset_DroneInformation',
    sql = setLset_DroneInformation,
    postgres_conn_id='pg_connection_1',
    dag=dag
)

truncateTableAndSetCet_DroneImage = PostgresOperator(
    task_id='truncateTableAndSetCet_DroneImage',
    sql= truncateTableAndSetCet_DroneImage,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
sourceToStage_DroneImage = PostgresOperator(
    task_id='sourceToStage_DroneImage',
    sql= sourceToStage_DroneImage,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
setLset_DroneImage = PostgresOperator(
    task_id='setLset_DroneImage',
    sql = setLset_DroneImage,
    postgres_conn_id='pg_connection_1',
    dag=dag
)

truncateTableAndSetCet_ChargingStation = PostgresOperator(
    task_id='truncateTableAndSetCet_ChargingStation',
    sql= truncateTableAndSetCet_ChargingStation,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
sourceToStage_ChargingStation = PostgresOperator(
    task_id='sourceToStage_ChargingStation',
    sql= sourceToStage_ChargingStation,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
setLset_ChargingStation = PostgresOperator(
    task_id='setLset_ChargingStation',
    sql = setLset_ChargingStation,
    postgres_conn_id='pg_connection_1',
    dag=dag
)

truncateTableAndSetCet_ChargingStatus = PostgresOperator(
    task_id='truncateTableAndSetCet_ChargingStatus',
    sql= truncateTableAndSetCet_ChargingStatus,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
sourceToStage_ChargingStatus = PostgresOperator(
    task_id='sourceToStage_ChargingStatus',
    sql= sourceToStage_ChargingStatus,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
setLset_ChargingStatus = PostgresOperator(
    task_id='setLset_ChargingStatus',
    sql = setLset_ChargingStatus,
    postgres_conn_id='pg_connection_1',
    dag=dag
)

truncateTableAndSetCet_Task = PostgresOperator(
    task_id='truncateTableAndSetCet_Task',
    sql= truncateTableAndSetCet_Task,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
sourceToStage_Task = PostgresOperator(
    task_id='sourceToStage_Task',
    sql= sourceToStage_Task,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
setLset_Task = PostgresOperator(
    task_id='setLset_Task',
    sql = setLset_Task,
    postgres_conn_id='pg_connection_1',
    dag=dag
)

truncateTableAndSetCet_Country >> sourceToStage_Country >> setLset_Country
truncateTableAndSetCet_Region >> sourceToStage_Region >> setLset_Region
truncateTableAndSetCet_Address >> sourceToStage_Address >> setLset_Address
truncateTableAndSetCet_Account >> sourceToStage_Account >> setLset_Account
truncateTableAndSetCet_UserInfo >> sourceToStage_UserInfo >> setLset_UserInfo
truncateTableAndSetCet_Field >> sourceToStage_Field >> setLset_Field
truncateTableAndSetCet_RubberTree >> sourceToStage_RubberTree >> setLset_RubberTree
truncateTableAndSetCet_RubberTreeInformation >> sourceToStage_RubberTreeInformation >> setLset_RubberTreeInformation
truncateTableAndSetCet_Plan >> sourceToStage_Plan >> setLset_Plan
truncateTableAndSetCet_PlanDetail >> sourceToStage_PlanDetail >> setLset_PlanDetail
truncateTableAndSetCet_Lidar >> sourceToStage_Lidar >> setLset_Lidar
truncateTableAndSetCet_Camera >> sourceToStage_Camera >> setLset_Camera
truncateTableAndSetCet_Radar >> sourceToStage_Radar >> setLset_Radar
truncateTableAndSetCet_SensorControlSystem >> sourceToStage_SensorControlSystem >> setLset_SensorControlSystem
truncateTableAndSetCet_Robot >> sourceToStage_Robot >> setLset_Robot
truncateTableAndSetCet_Energy >> sourceToStage_Energy >> setLset_Energy
truncateTableAndSetCet_RobotTapping >> sourceToStage_RobotTapping >> setLset_RobotTapping
truncateTableAndSetCet_Blade >> sourceToStage_Blade >> setLset_Blade
truncateTableAndSetCet_Environment >> sourceToStage_Environment >> setLset_Environment
truncateTableAndSetCet_Drone >> sourceToStage_Drone >> setLset_Drone
truncateTableAndSetCet_DroneInformation >> sourceToStage_DroneInformation >> setLset_DroneInformation
truncateTableAndSetCet_DroneImage >> sourceToStage_DroneImage >> setLset_DroneImage
truncateTableAndSetCet_ChargingStation >> sourceToStage_ChargingStation >> setLset_ChargingStation
truncateTableAndSetCet_ChargingStatus >> sourceToStage_ChargingStatus >> setLset_ChargingStatus
truncateTableAndSetCet_Task >> sourceToStage_Task >> setLset_Task