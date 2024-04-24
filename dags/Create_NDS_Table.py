import pandas as pd
import numpy as np
import requests
import time
import random
import pandas as pd
import json
import pendulum
from dags.sql.Sql_NDS_Table import *
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
    'start_date': pendulum.datetime(2024,4,24,tz='UTC'),
    'owner': 'airflow'
}

dag = DAG('Create_NDS_Table', default_args=default_args,schedule_interval='@once',catchup=False)

#---------------- NDS---------------------
create_table_NDS_Country = PostgresOperator(
    task_id='create_table_NDS_Country',
    postgres_conn_id='pg_connection_1',
    sql=create_table_NDS_Country,
    dag=dag
)
create_table_NDS_Region = PostgresOperator(
    task_id='create_table_NDS_Region',
    postgres_conn_id='pg_connection_1',
    sql=create_table_NDS_Region,
    dag=dag
)
create_table_NDS_Address = PostgresOperator(
    task_id='create_table_NDS_Address',
    postgres_conn_id='pg_connection_1',
    sql=create_table_NDS_Address,
    dag=dag
)
create_table_NDS_Account = PostgresOperator(
    task_id='create_table_NDS_Account',
    postgres_conn_id='pg_connection_1',
    sql=create_table_NDS_Account,
    dag=dag
)
create_table_NDS_UserInfo = PostgresOperator(
    task_id='create_table_NDS_UserInfo',
    postgres_conn_id='pg_connection_1',
    sql=create_table_NDS_UserInfo,
    dag=dag
)
create_table_NDS_Field = PostgresOperator(
    task_id='create_table_NDS_Field',
    postgres_conn_id='pg_connection_1',
    sql=create_table_NDS_Field,
    dag=dag
)
create_table_NDS_RubberTree = PostgresOperator(
    task_id='create_table_NDS_RubberTree',
    postgres_conn_id='pg_connection_1',
    sql=create_table_NDS_RubberTree,
    dag=dag
)
create_table_NDS_RubberTreeInformation = PostgresOperator(
    task_id='create_table_NDS_RubberTreeInformation',
    postgres_conn_id='pg_connection_1',
    sql=create_table_NDS_RubberTreeInformation,
    dag=dag
)
create_table_NDS_Plan = PostgresOperator(
    task_id='create_table_NDS_Plan',
    postgres_conn_id='pg_connection_1',
    sql=create_table_NDS_Plan,
    dag=dag
)
create_table_NDS_PlanDetail = PostgresOperator(
    task_id='create_table_NDS_PlanDetail',
    postgres_conn_id='pg_connection_1',
    sql=create_table_NDS_PlanDetail,
    dag=dag
)
create_table_NDS_Lidar = PostgresOperator(
    task_id='create_table_NDS_Lidar',
    postgres_conn_id='pg_connection_1',
    sql=create_table_NDS_Lidar,
    dag=dag
)
create_table_NDS_Camera = PostgresOperator(
    task_id='create_table_NDS_Camera',
    postgres_conn_id='pg_connection_1',
    sql=create_table_NDS_Camera,
    dag=dag
)
create_table_NDS_Radar = PostgresOperator(
    task_id='create_table_NDS_Radar',
    postgres_conn_id='pg_connection_1',
    sql=create_table_NDS_Radar,
    dag=dag
)
create_table_NDS_SensorControlSystem = PostgresOperator(
    task_id='create_table_NDS_SensorControlSystem',
    postgres_conn_id='pg_connection_1',
    sql=create_table_NDS_SensorControlSystem,
    dag=dag
)
create_table_NDS_Robot = PostgresOperator(  
    task_id='create_table_NDS_Robot',
    postgres_conn_id='pg_connection_1',
    sql=create_table_NDS_Robot,
    dag=dag
)
create_table_NDS_Energy = PostgresOperator(
    task_id='create_table_NDS_Energy',
    postgres_conn_id='pg_connection_1',
    sql=create_table_NDS_Energy,
    dag=dag
)
create_table_NDS_RobotTapping = PostgresOperator(
    task_id='create_table_NDS_RobotTapping',
    postgres_conn_id='pg_connection_1',
    sql=create_table_NDS_RobotTapping,
    dag=dag
)
create_table_NDS_Blade = PostgresOperator(
    task_id='create_table_NDS_Blade',
    postgres_conn_id='pg_connection_1',
    sql=create_table_NDS_Blade,
    dag=dag
)
create_table_NDS_Environment = PostgresOperator(
    task_id='create_table_NDS_Environment',
    postgres_conn_id='pg_connection_1',
    sql=create_table_NDS_Environment,
    dag=dag
)
create_table_NDS_Drone = PostgresOperator(
    task_id='create_table_NDS_Drone',
    postgres_conn_id='pg_connection_1',
    sql=create_table_NDS_Drone,
    dag=dag
)
create_table_NDS_DroneInformation = PostgresOperator(
    task_id='create_table_NDS_DroneInformation',
    postgres_conn_id='pg_connection_1',
    sql=create_table_NDS_DroneInformation,
    dag=dag
)
create_table_NDS_DroneImage = PostgresOperator(
    task_id='create_table_NDS_DroneImage',
    postgres_conn_id='pg_connection_1',
    sql=create_table_NDS_DroneImage,
    dag=dag
)
create_table_NDS_ChargingStation = PostgresOperator(
    task_id='create_table_NDS_ChargingStation',
    postgres_conn_id='pg_connection_1',
    sql=create_table_NDS_ChargingStation,
    dag=dag
)
create_table_NDS_ChargingStatus = PostgresOperator(
    task_id='create_table_NDS_ChargingStatus',
    postgres_conn_id='pg_connection_1',
    sql=create_table_NDS_ChargingStatus,
    dag=dag
)
create_table_NDS_Task = PostgresOperator(
    task_id='create_table_NDS_Task',
    postgres_conn_id='pg_connection_1',
    sql=create_table_NDS_Task,
    dag=dag
)

# [create_table_NDS_Country, create_table_NDS_Account, create_table_NDS_Plan, create_table_NDS_Lidar, create_table_NDS_Camera, create_table_NDS_Radar, create_table_NDS_Robot, create_table_NDS_ChargingStation], [create_table_NDS_Region, create_table_NDS_SensorControlSystem, create_table_NDS_ChargingStatus, create_table_NDS_Task, create_table_NDS_Energy], [ create_table_NDS_Address, create_table_NDS_Field, create_table_NDS_Drone], [ create_table_NDS_UserInfo, create_table_NDS_RubberTree, create_table_NDS_PlanDetail, create_table_NDS_DroneInformation],[ create_table_NDS_RubberTreeInformation, create_table_NDS_RobotTapping, create_table_NDS_DroneImage],[create_table_NDS_Blade, create_table_NDS_Environment]


[create_table_NDS_Country, create_table_NDS_Account, create_table_NDS_Plan, create_table_NDS_Lidar, create_table_NDS_Camera, create_table_NDS_Radar, create_table_NDS_Robot
] >> create_table_NDS_ChargingStation >> [create_table_NDS_Region, create_table_NDS_SensorControlSystem, create_table_NDS_ChargingStatus, create_table_NDS_Task
] >> create_table_NDS_Energy >>[ create_table_NDS_Address, create_table_NDS_Field] >> create_table_NDS_Drone >> [ create_table_NDS_UserInfo, create_table_NDS_RubberTree, create_table_NDS_PlanDetail
] >> create_table_NDS_DroneInformation >> [ create_table_NDS_RubberTreeInformation, create_table_NDS_RobotTapping] >> create_table_NDS_DroneImage >> [create_table_NDS_Blade, create_table_NDS_Environment]
