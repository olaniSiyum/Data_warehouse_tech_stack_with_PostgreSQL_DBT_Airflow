from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import psycopg2
import sys,os
import pandas as pd 
from sqlalchemy import create_engine
import random
dag_path = os.getcwd()
sys.path.append('/arehouse_tech_stack_with_PostgreSQL_DBT_Airflow/airflow/dagshome/olani/Documents/week2/Data_w')
from script.extract_data_source import get_data
from script.transform_data import transform_data
from script.load_data import load_data
from script.extract_data_source import ELT
from airflow.utils.dates import days_ago
import requests
import json

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

elt = ELT(read_dag_path=f"{dag_path }/home/olani/Downloads/20181024_d1_0830_0900.csv",
         save_dag_path=f"{dag_path }/processed_data/")
# Define the default dag arguments.
default_args = {
    'owner': 'airflow',
    'start_date': days_ago(5)
}
ingestion_dag = DAG(
    'traffic_data_ingestion',
    default_args=default_args,
    description='Aggregates booking records for data analysis',
    schedule_interval=timedelta(hours=1),
    catchup=False,
    user_defined_macros={'date_to_millis': elt.execution_date_to_millis}
)


# Define the DAG
dag = DAG(
    dag_id='new_dag',
    default_args=default_args,
    start_date=datetime(2023, 12, 21),
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

