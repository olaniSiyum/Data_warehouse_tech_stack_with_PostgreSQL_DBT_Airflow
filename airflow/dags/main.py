from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import psycopg2
import sys
import pandas as pd 
from sqlalchemy import create_engine
import random
sys.path.append('/home/olani/Documents/week2/Data_warehouse_tech_stack_with_PostgreSQL_DBT_Airflow/airflow/dags')
from script.extract_data_source import get_data
from script.transform_data import transform_data
from script.load_data import load_data
import requests
import json
import os

# Function to simulate data loading into PostgreSQL
def load_data_to_postgres():
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname='week2',
        user='postgres',
        password='pgadmin',
        host='localhost',
        port='5432'
    )

    # Create a cursor object using the connection
    cursor = conn.cursor()

    # Simulate data insertion
    for i in range(10):  # Simulate loading 10 rows of data
        data = (f"Data_{i}", random.randint(1, 100))  # Example data
        cursor.execute("INSERT INTO your_table_name (column1, column2) VALUES (%s, %s)", data)

    # Commit changes and close the connection
    conn.commit()
    conn.close()
# Define the default dag arguments.
default_args = {
    'owner': 'admin',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


# Define the DAG
dag = DAG(
    dag_id='new_dag',
    default_args=default_args,
    start_date=datetime(2023, 12, 19),
    schedule_interval= "@daily" ) 

task1 = PythonOperator(
    task_id='get_data',
    provide_context=True,
    python_callable=get_data,
    dag=dag)

# Second task is to transform the data
task2 = PythonOperator(
    task_id='load_data',
    provide_context=True,
    python_callable=load_data,
    dag=dag)

# Third task is to transform data into the database.
task3 = PythonOperator(
    task_id='transform_data',
    provide_context=True,
    python_callable=transform_data,
    dag=dag)

# Set task1 "upstream" of task2
# task1 must be completed before task2 can be started
task1 >> task2 >> task3

