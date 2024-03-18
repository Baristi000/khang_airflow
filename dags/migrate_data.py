# from airflow import DAG
# from airflow.operators.mysql_operator import MySqlOperator
# from airflow.providers.google.cloud.operators.bigquery import (
#     BigQueryUpdateTableOperator
# )
# from datetime import datetime

# default_args = {
#     'owner': 'airflow',
#     'start_date': datetime(2024, 3, 13),
#     'retries': 1,
# }

# get_data_query = '''
# SELECT * FROM test_db.test_table;
# '''
# push_data_query = '''

# '''