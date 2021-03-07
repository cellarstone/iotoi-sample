from airflow.decorators import dag, task
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from faker import Faker
from typing import List, Dict, Any
import random
from airflow.utils.dates import days_ago
import uuid

fake = Faker("en_US")

# ----------------------------------------------------------------
# Default Arguments
# ----------------------------------------------------------------
default_args = {"owner": "iotoi"}

# ----------------------------------------------------------------
# DAG definition
# ----------------------------------------------------------------
@dag(
    default_args=default_args,
    schedule_interval=None,
    start_date=days_ago(1),
    tags=["iotoi-samples"],
)
def save_to_minio_2():
    @task(multiple_outputs=True)
    def generate() -> Dict[str, Any]:
        my_dict = {
            "foo": random.randint(0, 100),
            "bar": {
                "baz": fake.name(),
                "poo": float(random.randrange(155, 389)) / 100,
            },
        }
        return my_dict

    @task()
    def write_text_file(ds, **kwargs):
        with open("/tmp/test.txt", "w") as fp:
            # Add file generation/processing step here, E.g.:
            fp.write("Now the file has more content!\n")
            fp.write(str(ds))

        # Upload generated file to Minio
        s3 = S3Hook("local_minio")
        s3.load_file(
            "/tmp/test.txt",
            key=f"my-test-file-2.txt-{uuid.uuid4()}",
            bucket_name="my-first-bucket",
        )

    rndJson = generate()
    write_text_file(str(rndJson))


global_save_to_minio_2 = save_to_minio_2()
