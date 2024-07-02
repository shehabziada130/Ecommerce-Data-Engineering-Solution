from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from airflow.utils.dates import days_ago

dag_arguments={
    'owner':'airflow',
    'start_date':days_ago(0),
    'email':['shehab@gmail.com']
}

dag=DAG(
    'process_web_log',
    default_args=dag_arguments,
    description='a process web log dag runs daily',
    schedule_interval='@daily',
)

extract_task=BashOperator(
    task_id='extract_data',
    bash_command='cut -f1 -d" " home/project/airflow/dags/capstone/accesslog.txt > extracted_data.txt',
    dag=dag,
)

transform_task=BashOperator(
    task_id='transform_data',
    bash_command='grep -v "198.46.149.143" /home/project/airflow/dags/extracted_data.txt > transformed_data.txt',
    dag=dag,
)

load_task=BashOperator(
    task_id='load_data',
    bash_command='tar -czvf weblog.tar.gz transformed_data.txt',
    dag=dag,
)

extract_task >> transform_task >> load_task