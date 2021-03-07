from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

from airflow.providers.amazon.aws.sensors.s3_key import S3KeySensor

default_args = {
    "owner": "iotoi",
    "start_date": days_ago(1),
}

dag = DAG(
    "check_minio_1",
    default_args=default_args,
    schedule_interval="@once",
    tags=["iotoi-samples"],
)


t1 = BashOperator(
    task_id="bash_test",
    bash_command='echo "hello, it should work" > s3_conn_test.txt',
    dag=dag,
)

sensor = S3KeySensor(
    task_id="check_s3_for_file_in_s3",
    bucket_key="*",
    bucket_name="my-first-bucket",
    wildcard_match=True,
    aws_conn_id="local_minio",
    poke_interval=10,
    dag=dag,
)

t1.set_upstream(sensor)