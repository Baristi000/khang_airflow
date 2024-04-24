import pandas as pd
import numpy as np
import requests
import time
import random
import pandas as pd
import json
import pendulum
from dags.sql.Sql_Stage_Table import *
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
    'start_date': pendulum.datetime(2024,4,24,tz='UTC'),
    'owner': 'airflow'
}

dag = DAG('Create_Stage_Table', default_args=default_args,schedule_interval='@once',catchup=False)

#---------------- Stage---------------------
create_table_Stage_Country = PostgresOperator(
    task_id='create_table_Stage_Country',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Stage_Country,
    dag=dag
)
create_table_Stage_Region = PostgresOperator(
    task_id='create_table_Stage_Region',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Stage_Region,
    dag=dag
)
create_table_Stage_Address = PostgresOperator(
    task_id='create_table_Stage_Address',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Stage_Address,
    dag=dag
)
create_table_Stage_Account = PostgresOperator(
    task_id='create_table_Stage_Account',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Stage_Account,
    dag=dag
)
create_table_Stage_UserInfo = PostgresOperator(
    task_id='create_table_Stage_UserInfo',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Stage_UserInfo,
    dag=dag
)
create_table_Stage_Field = PostgresOperator(
    task_id='create_table_Stage_Field',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Stage_Field,
    dag=dag
)
create_table_Stage_RubberTree = PostgresOperator(
    task_id='create_table_Stage_RubberTree',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Stage_RubberTree,
    dag=dag
)
create_table_Stage_RubberTreeInformation = PostgresOperator(
    task_id='create_table_Stage_RubberTreeInformation',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Stage_RubberTreeInformation,
    dag=dag
)
create_table_Stage_Plan = PostgresOperator(
    task_id='create_table_Stage_Plan',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Stage_Plan,
    dag=dag
)
create_table_Stage_PlanDetail = PostgresOperator(
    task_id='create_table_Stage_PlanDetail',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Stage_PlanDetail,
    dag=dag
)
create_table_Stage_Lidar = PostgresOperator(
    task_id='create_table_Stage_Lidar',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Stage_Lidar,
    dag=dag
)
create_table_Stage_Camera = PostgresOperator(
    task_id='create_table_Stage_Camera',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Stage_Camera,
    dag=dag
)
create_table_Stage_Radar = PostgresOperator(
    task_id='create_table_Stage_Radar',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Stage_Radar,
    dag=dag
)
create_table_Stage_SensorControlSystem = PostgresOperator(
    task_id='create_table_Stage_SensorControlSystem',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Stage_SensorControlSystem,
    dag=dag
)
create_table_Stage_Robot = PostgresOperator(  
    task_id='create_table_Stage_Robot',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Stage_Robot,
    dag=dag
)
create_table_Stage_Energy = PostgresOperator(
    task_id='create_table_Stage_Energy',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Stage_Energy,
    dag=dag
)
create_table_Stage_RobotTapping = PostgresOperator(
    task_id='create_table_Stage_RobotTapping',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Stage_RobotTapping,
    dag=dag
)
create_table_Stage_Blade = PostgresOperator(
    task_id='create_table_Stage_Blade',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Stage_Blade,
    dag=dag
)
create_table_Stage_Environment = PostgresOperator(
    task_id='create_table_Stage_Environment',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Stage_Environment,
    dag=dag
)
create_table_Stage_Drone = PostgresOperator(
    task_id='create_table_Stage_Drone',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Stage_Drone,
    dag=dag
)
create_table_Stage_DroneInformation = PostgresOperator(
    task_id='create_table_Stage_DroneInformation',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Stage_DroneInformation,
    dag=dag
)
create_table_Stage_DroneImage = PostgresOperator(
    task_id='create_table_Stage_DroneImage',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Stage_DroneImage,
    dag=dag
)
create_table_Stage_ChargingStation = PostgresOperator(
    task_id='create_table_Stage_ChargingStation',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Stage_ChargingStation,
    dag=dag
)
create_table_Stage_ChargingStatus = PostgresOperator(
    task_id='create_table_Stage_ChargingStatus',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Stage_ChargingStatus,
    dag=dag
)
create_table_Stage_Task = PostgresOperator(
    task_id='create_table_Stage_Task',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Stage_Task,
    dag=dag
)
