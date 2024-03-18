from airflow import DAG
# from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from datetime import datetime
from airflow.providers.google.cloud.operators.bigquery import (
    BigQueryCreateEmptyDatasetOperator,
    BigQueryInsertJobOperator,
)

# Định nghĩa các tham số cho DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 13),
    'retries': 1,
}

# Khởi tạo DAG
# dag = DAG(
#     'create_bigquery_table_dag',
#     default_args=default_args,
#     description='A DAG to create a table in BigQuery',
#     schedule_interval=None
# )

# Truy vấn SQL để tạo bảng trong BigQuery
create_table_query = """
CREATE OR REPLACE TABLE `test_ds.test_table` (
  id INT64,
  name STRING,
  age INT64
)
"""

# Operator để thực hiện truy vấn SQL và tạo bảng trong BigQuery
with DAG(
    dag_id="create_bigquery_table_dag",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description='A DAG to create a table in BigQuery',
) as dag:
    create_dataset_task = BigQueryCreateEmptyDatasetOperator(
        task_id="create_dataset",
        dataset_id="test_ds",
        location="eu",
        gcp_conn_id="googlebigquery",
    )
    create_simple_table_task = BigQueryInsertJobOperator(
        task_id="create_simple_table",
        gcp_conn_id="googlebigquery",
        configuration={
            "query": {
                "query": create_table_query,
                "useLegacySql": False,
            }
        },
    )



# Sắp xếp các task trong DAG
create_dataset_task >> create_simple_table_task
