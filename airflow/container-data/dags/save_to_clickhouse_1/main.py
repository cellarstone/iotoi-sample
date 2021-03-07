from airflow.decorators import dag, task
from airflow.utils.dates import days_ago

from clickhouse_driver import connect

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
def save_to_clickhouse_1():
    conn = connect("clickhouse://192.168.0.9")

    @task()
    def log(ds):
        print("Should be saved in clickhouse")
        print(ds)

    @task()
    def save():
        cursor = conn.cursor()
        cursor.execute(
            """
                INSERT INTO test.testtable2
                (id, `hostname`, `ip`, `random`)
                VALUES(0, 'somename1','192.168.0.1', '3892432');
            """
        )

        cursor.close()

    aaa = save()
    log(aaa)


global_save_to_clickhouse_1 = save_to_clickhouse_1()
