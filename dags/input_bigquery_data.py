from airflow import DAG 
from airflow.operators.python import BranchPythonOperator
from airflow.providers.google.cloud.operators.bigquery import (
    BigQueryInsertJobOperator
)
from datetime import datetime
from airflow.operators.empty import EmptyOperator
import random
from uuid import uuid1

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 13),
    'retries': 1,
}




with DAG(
    'input_data_to_bigquery',
    default_args=default_args,
    description='A DAG to input data to bigquery table',
    schedule_interval=None
) as dag:
    i = 1
    INSERT_ROWS_QUERY = f"INSERT test_ds.test_table VALUES ({i},TrieuLe_{i},{12+i})"
    for i in range(2,5):
        INSERT_ROWS_QUERY += f",({i},TrieuLe_{i},{12+i})"
    insert_task = BigQueryInsertJobOperator(
                task_id="insert_query_job",
                configuration={
                    "query": {
                        "query": INSERT_ROWS_QUERY,
                        "useLegacySql": False,
                        "priority": "BATCH",
                    }
                },
                gcp_conn_id="googlebigquery",
            )
    i=2
insert_task