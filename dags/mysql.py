from airflow import DAG
from airflow.operators.mysql_operator import MySqlOperator
from datetime import datetime

# Định nghĩa các tham số cho DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 13),
    'retries': 1,
}

# Khởi tạo DAG
dag = DAG(
    'create_mysql_table_dag',
    default_args=default_args,
    description='A DAG to create a table in MySQL Server',
    schedule_interval=None
)

# Operator để thực thi truy vấn SQL để tạo bảng trong MySQL
create_table_task = MySqlOperator(
    task_id='create_table',
    mysql_conn_id='KhangVPS',  # Tên của MySQL connection được cấu hình trong Airflow
    sql='''
    use test_db;
    CREATE TABLE IF NOT EXISTS test_table (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    )''',
    dag=dag
)

create_schema_task = MySqlOperator(
    task_id='create_database',
    mysql_conn_id='KhangVPS',  # Tên của MySQL connection được cấu hình trong Airflow
    sql='''CREATE DATABASE test_db;''',
    dag=dag
)


# Sắp xếp các task trong DAG
create_schema_task >> create_table_task
