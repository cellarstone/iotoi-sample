from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
from typing import List, Dict, Any
import requests

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
def get_http():
    URL = "https://randomuser.me/api/"

    @task()
    def log(rnd_json: Dict[str, Any]):
        print("We get the response via HTTP")
        print(rnd_json)

    @task(multiple_outputs=True)
    def get_from_http() -> Dict[str, Any]:
        r = requests.get(url=URL)
        data = r.json()
        return data

    res = get_from_http()
    log(res)


global_get_http = get_http()
