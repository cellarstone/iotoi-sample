from datetime import datetime, timedelta
from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
from airflow.providers.apache.spark.operators.spark_submit import (
    SparkSubmitOperator,
)


# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    "owner": "iotoi",
}


@dag(
    default_args=default_args,
    schedule_interval=None,
    start_date=days_ago(1),
    tags=["iotoi-samples"],
)
def spark_submit_1():
    @task()
    def log_start():
        print("-----------------------Start-----------------------")

    @task()
    def log_end():
        print("-----------------------Start-----------------------")

    log_start()
    SparkSubmitOperator(
        task_id="spark_submit_1_task",
        name="spark_submit_1_task",
        conn_id="local_spark",
        application="/spark-scripts/the-simplest/main.py",
    )
    log_end()


global_spark_submit_1 = spark_submit_1()