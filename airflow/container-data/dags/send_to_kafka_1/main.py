from airflow.decorators import dag, task
from airflow.utils.dates import days_ago

from kafka import KafkaProducer

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
def send_to_kafka_1():
    @task()
    def log(ds):
        print("Should be send in kafka")
        print(ds)

    @task()
    def send():
        producer = KafkaProducer(bootstrap_servers="192.168.0.9:9092")
        producer.send("test-topic-1", b"Hello, World!")
        producer.send(
            "test-topic-1", key=b"message-two", value=b"This is Kafka-Python"
        )

    aaa = send()
    log(aaa)


global_send_to_kafka_1 = send_to_kafka_1()
