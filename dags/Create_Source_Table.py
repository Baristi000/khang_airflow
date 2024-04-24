import pandas as pd
import numpy as np
import requests
import time
import random
import pandas as pd
import json
import pendulum
from dags.sql.Sql_Source_Table import *
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
    'start_date': pendulum.datetime(2024,4,24,tz='UTC'),
    'owner': 'airflow'
}

dag = DAG('Create_Source_Table', default_args=default_args,schedule_interval='@once',catchup=False)

#---------------- Source---------------------
create_table_Source_Country = PostgresOperator(
    task_id='create_table_Source_Country',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Source_Country,
    dag=dag
)
create_table_Source_Region = PostgresOperator(
    task_id='create_table_Source_Region',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Source_Region,
    dag=dag
)
create_table_Source_Address = PostgresOperator(
    task_id='create_table_Source_Address',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Source_Address,
    dag=dag
)
create_table_Source_Account = PostgresOperator(
    task_id='create_table_Source_Account',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Source_Account,
    dag=dag
)
create_table_Source_UserInfo = PostgresOperator(
    task_id='create_table_Source_UserInfo',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Source_UserInfo,
    dag=dag
)
create_table_Source_Field = PostgresOperator(
    task_id='create_table_Source_Field',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Source_Field,
    dag=dag
)
create_table_Source_RubberTree = PostgresOperator(
    task_id='create_table_Source_RubberTree',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Source_RubberTree,
    dag=dag
)
create_table_Source_RubberTreeInformation = PostgresOperator(
    task_id='create_table_Source_RubberTreeInformation',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Source_RubberTreeInformation,
    dag=dag
)
create_table_Source_Plan = PostgresOperator(
    task_id='create_table_Source_Plan',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Source_Plan,
    dag=dag
)
create_table_Source_PlanDetail = PostgresOperator(
    task_id='create_table_Source_PlanDetail',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Source_PlanDetail,
    dag=dag
)
create_table_Source_Lidar = PostgresOperator(
    task_id='create_table_Source_Lidar',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Source_Lidar,
    dag=dag
)
create_table_Source_Camera = PostgresOperator(
    task_id='create_table_Source_Camera',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Source_Camera,
    dag=dag
)
create_table_Source_Radar = PostgresOperator(
    task_id='create_table_Source_Radar',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Source_Radar,
    dag=dag
)
create_table_Source_SensorControlSystem = PostgresOperator(
    task_id='create_table_Source_SensorControlSystem',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Source_SensorControlSystem,
    dag=dag
)
create_table_Source_Robot = PostgresOperator(  
    task_id='create_table_Source_Robot',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Source_Robot,
    dag=dag
)
create_table_Source_Energy = PostgresOperator(
    task_id='create_table_Source_Energy',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Source_Energy,
    dag=dag
)
create_table_Source_RobotTapping = PostgresOperator(
    task_id='create_table_Source_RobotTapping',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Source_RobotTapping,
    dag=dag
)
create_table_Source_Blade = PostgresOperator(
    task_id='create_table_Source_Blade',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Source_Blade,
    dag=dag
)
create_table_Source_Environment = PostgresOperator(
    task_id='create_table_Source_Environment',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Source_Environment,
    dag=dag
)
create_table_Source_Drone = PostgresOperator(
    task_id='create_table_Source_Drone',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Source_Drone,
    dag=dag
)
create_table_Source_DroneInformation = PostgresOperator(
    task_id='create_table_Source_DroneInformation',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Source_DroneInformation,
    dag=dag
)
create_table_Source_DroneImage = PostgresOperator(
    task_id='create_table_Source_DroneImage',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Source_DroneImage,
    dag=dag
)
create_table_Source_ChargingStation = PostgresOperator(
    task_id='create_table_Source_ChargingStation',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Source_ChargingStation,
    dag=dag
)
create_table_Source_ChargingStatus = PostgresOperator(
    task_id='create_table_Source_ChargingStatus',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Source_ChargingStatus,
    dag=dag
)
create_table_Source_Task = PostgresOperator(
    task_id='create_table_Source_Task',
    postgres_conn_id='pg_connection_1',
    sql=create_table_Source_Task,
    dag=dag
)