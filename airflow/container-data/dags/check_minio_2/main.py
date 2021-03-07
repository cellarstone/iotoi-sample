from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
from typing import List, Dict, Any
from airflow.providers.amazon.aws.sensors.s3_key import S3KeySensor
import random


# ----------------------------------------------------------------
# Default Arguments
# ----------------------------------------------------------------
default_args = {
    "owner": "iotoi",
}

# ----------------------------------------------------------------
# DAG definition
# ----------------------------------------------------------------
@dag(
    default_args=default_args,
    schedule_interval="@once",
    start_date=days_ago(1),
    tags=["iotoi-samples"],
)
def check_minio_2():
    @task()
    def log():
        print("Something happened in bucket")

    sensor = S3KeySensor(
        task_id="check_s3_for_file_in_s3",
        bucket_key="s3://my-first-bucket/my-test-file-2.txt-*",
        wildcard_match=True,
        aws_conn_id="local_minio",
    )

    aaa = log()

    sensor >> aaa


global_check_minio_2 = check_minio_2()
