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
def get_from_clickhouse_1():
    conn = connect("clickhouse://192.168.0.9")

    @task()
    def log(ds):
        print("Should be saved in clickhouse")
        print(ds)

    @task()
    def save():
        cursor = conn.cursor()
        result = cursor.execute(
            """
                SELECT * FROM test.testtable2
            """
        )
        cursor.fetchall()
        print(result)
        cursor.close()
        return result

    aaa = save()
    log(aaa)


global_get_from_clickhouse_1 = get_from_clickhouse_1()
