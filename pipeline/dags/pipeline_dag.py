from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

try:
    from airflow.utils import timezone #airflow.utils.timezone is available from v1.10 onwards
    now = timezone.utcnow
except ImportError:
    now = datetime.utcnow

default_args = {
    'owner': 'Abe.Chen',
    'depends_on_past': False,
    'start_date': now() - timedelta(days=1),
    'email': ['abe.chen@example.com'],
    'email_on_failure': False,
    'email_on_retry': False
}

dag = DAG('ml-lifecyele-demo', default_args=default_args, schedule_interval=timedelta(days=1))

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='task 1',
    bash_command='echo task1',
    dag=dag)

t2 = BashOperator(
    task_id='task 2',
    bash_command='echo task2',
    dag=dag)

t3 = BashOperator(
    task_id='task 3',
    bash_command="echo task3",
    dag=dag)

t1 >> t2
t2 >> t3
