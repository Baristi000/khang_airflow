import pandas as pd
import numpy as np
import requests
import time
import random
import pandas as pd
import json
import pendulum
from dags.sql.StageToNDS import *
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
    'start_date': pendulum.datetime(2024,4,21,tz='UTC'),
    'owner': 'airflow'
}
dag = DAG('StageToNDS_Rubber', default_args=default_args,schedule_interval='@once',catchup=False)

StageToNDS_Country = PostgresOperator(
    task_id='StageToNDS_Country',
    sql= StageToNDS_Country,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
StageToNDS_Region = PostgresOperator(
    task_id='StageToNDS_Region',
    sql= StageToNDS_Region,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
StageToNDS_Address = PostgresOperator(
    task_id='StageToNDS_Address',
    sql= StageToNDS_Address,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
StageToNDS_Account = PostgresOperator(
    task_id='StageToNDS_Account',
    sql= StageToNDS_Account,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
StageToNDS_UserInfo = PostgresOperator(
    task_id='StageToNDS_UserInfo',
    sql= StageToNDS_UserInfo,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
StageToNDS_Field = PostgresOperator(
    task_id='StageToNDS_Field',
    sql= StageToNDS_Field,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
StageToNDS_RubberTree = PostgresOperator(
    task_id='StageToNDS_RubberTree',
    sql= StageToNDS_RubberTree,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
StageToNDS_RubberTreeInformation = PostgresOperator(
    task_id='StageToNDS_RubberTreeInformation',
    sql= StageToNDS_RubberTreeInformation,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
StageToNDS_Plan = PostgresOperator(
    task_id='StageToNDS_Plan',
    sql= StageToNDS_Plan,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
StageToNDS_PlanDetail = PostgresOperator(
    task_id='StageToNDS_PlanDetail',
    sql= StageToNDS_PlanDetail,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
StageToNDS_Lidar = PostgresOperator(
    task_id='StageToNDS_Lidar',
    sql= StageToNDS_Lidar,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
StageToNDS_Camera = PostgresOperator(
    task_id='StageToNDS_Camera',
    sql= StageToNDS_Camera,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
StageToNDS_Radar = PostgresOperator(
    task_id='StageToNDS_Radar',
    sql= StageToNDS_Radar,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
StageToNDS_SensorControlSystem = PostgresOperator(
    task_id='StageToNDS_SensorControlSystem',
    sql= StageToNDS_SensorControlSystem,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
StageToNDS_Robot = PostgresOperator(
    task_id='StageToNDS_Robot',
    sql= StageToNDS_Robot,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
StageToNDS_Energy = PostgresOperator(
    task_id='StageToNDS_Energy',
    sql= StageToNDS_Energy,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
StageToNDS_RobotTapping = PostgresOperator(
    task_id='StageToNDS_RobotTapping',
    sql= StageToNDS_RobotTapping,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
StageToNDS_Blade = PostgresOperator(
    task_id='StageToNDS_Blade',
    sql= StageToNDS_Blade,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
StageToNDS_Environment = PostgresOperator(
    task_id='StageToNDS_Environment',
    sql= StageToNDS_Environment,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
StageToNDS_Drone = PostgresOperator(
    task_id='StageToNDS_Drone',
    sql= StageToNDS_Drone,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
StageToNDS_DroneInformation = PostgresOperator(
    task_id='StageToNDS_DroneInformation',
    sql= StageToNDS_DroneInformation,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
StageToNDS_DroneImage = PostgresOperator(
    task_id='StageToNDS_DroneImage',
    sql= StageToNDS_DroneImage,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
StageToNDS_ChargingStation = PostgresOperator(
    task_id='StageToNDS_ChargingStation',
    sql= StageToNDS_ChargingStation,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
StageToNDS_ChargingStatus = PostgresOperator(
    task_id='StageToNDS_ChargingStatus',
    sql= StageToNDS_ChargingStatus,
    postgres_conn_id='pg_connection_1',
    dag=dag
)
StageToNDS_Task = PostgresOperator(
    task_id='StageToNDS_Task',
    sql= StageToNDS_Task,
    postgres_conn_id='pg_connection_1',
    dag=dag
)

[StageToNDS_Country, StageToNDS_Account, StageToNDS_Plan, StageToNDS_Lidar, StageToNDS_Camera, StageToNDS_Radar, StageToNDS_Robot
] >> StageToNDS_ChargingStation >> [StageToNDS_Region, StageToNDS_SensorControlSystem, StageToNDS_Task
] >> StageToNDS_Energy >>[ StageToNDS_Address, StageToNDS_Field] >> StageToNDS_Drone >> [ StageToNDS_ChargingStatus, StageToNDS_UserInfo, 
StageToNDS_RubberTree, StageToNDS_PlanDetail] >> StageToNDS_DroneInformation >> [ StageToNDS_RubberTreeInformation, StageToNDS_RobotTapping
] >> StageToNDS_DroneImage >> [StageToNDS_Blade, StageToNDS_Environment]

