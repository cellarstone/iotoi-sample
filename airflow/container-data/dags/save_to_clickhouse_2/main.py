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
def save_to_clickhouse_2():
    client = Client("192.168.0.9", database="test")

    @task()
    def log(ds):
        print("Should be saved in clickhouse")
        print(ds)

    @task()
    def save():
        result = client.execute("SELECT now(), version()")
        print(result)
        client.execute(
            """
                INSERT INTO test.testtable2
                (id, `hostname`, `ip`, `random`)
                VALUES(0, 'somename2','192.168.0.1', '3892432');
            """
        )

    aaa = save()
    log(aaa)


global_save_to_clickhouse_2 = save_to_clickhouse_2()
