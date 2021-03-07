from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
import uuid

DEFAULT_ARGS = {
    "owner": "iotoi",
    "depends_on_past": False,
    "start_date": datetime(2020, 1, 13),
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "save_to_minio",
    default_args=DEFAULT_ARGS,
    schedule_interval="@once",
    tags=["iotoi-samples"],
)


def write_text_file(ds, **kwargs):
    with open("/tmp/test.txt", "w") as fp:
        # Add file generation/processing step here, E.g.:
        fp.write("Now the file has more content!\n")
        fp.write(ds)

    # Upload generated file to Minio
    s3 = S3Hook("local_minio")
    s3.load_file(
        "/tmp/test.txt",
        key=f"my-test-file-1.txt-{uuid.uuid4()}",
        bucket_name="my-first-bucket",
    )


# Create a task to call your processing function
t1 = PythonOperator(
    task_id="generate_and_upload_to_s3",
    provide_context=True,
    python_callable=write_text_file,
    dag=dag,
)
