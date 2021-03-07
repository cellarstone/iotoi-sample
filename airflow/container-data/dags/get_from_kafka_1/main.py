from airflow.decorators import dag, task
from airflow.utils.dates import days_ago

from kafka import KafkaConsumer

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
def get_from_kafka_1():
    @task()
    def log(ds):
        print("Should be send in kafka")
        print(ds)

    @task()
    def get():
        consumer = KafkaConsumer(
            "test-topic-1", bootstrap_servers="192.168.0.9:9092"
        )
        for msg in consumer:
            print(msg)

    aaa = get()
    log(aaa)


global_get_from_kafka_1 = get_from_kafka_1()
