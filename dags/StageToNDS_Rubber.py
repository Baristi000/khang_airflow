import pandas as pd
import numpy as np
import requests
import time
import random
import pandas as pd
import json
import pendulum
from dags.sql.create_table import *
from dags.sql.SourceToStage import *
# import dags.create_table as qr
from airflow import DAG
from airflow.operators.python import PythonOperator
# from airflow.models.connection import Connection
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
    'start_date': pendulum.datetime(2024,4,21,tz='UTC'),
    'owner': 'airflow'
}
dag = DAG('StageToNDS_Rubber', default_args=default_args,schedule_interval='@once',catchup=False)


create_table_Country = PostgresOperator(
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
create_table_Country >> StageToNDS_Country