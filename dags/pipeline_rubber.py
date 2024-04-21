import pandas as pd
import numpy as np
import requests
import time
import random
import pandas as pd
import json
import pendulum
# import staging as stg
import create_table as qr
# import insertion as ins
from airflow import DAG
from airflow.operators.python import PythonOperator
# from airflow.models.connection import Connection
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
    'start_date': pendulum.datetime(2024,4,20,tz='UTC'),
    'owner': 'airflow'
}
dag = DAG('rubber', default_args=default_args,schedule_interval='@once',catchup=False)

create_written_table = PostgresOperator(
    task_id='create_written_table',
    postgres_conn_id='postgres_connection',
    sql=qr.create_table_written,
    dag=dag
)
create_written_table