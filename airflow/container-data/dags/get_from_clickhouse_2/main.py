from airflow.decorators import dag, task
from airflow.utils.dates import days_ago

from clickhouse_driver import Client

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
def get_from_clickhouse_2():
    client = Client("192.168.0.9", database="test")

    @task()
    def log(ds):
        print("Should be saved in clickhouse")
        print(ds)

    @task()
    def save():
        result = client.execute("SELECT * FROM test.testtable2")
        print(result)
        return result

    aaa = save()
    log(aaa)


global_get_from_clickhouse_2 = get_from_clickhouse_2()
