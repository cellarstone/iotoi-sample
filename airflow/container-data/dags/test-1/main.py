import json

from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
import random

import json
from faker import Faker
from random import randint
from typing import List, Dict, Any

fake = Faker("en_US")

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
def test_1():
    @task()
    def generate() -> Dict[str, Any]:
        my_dict = {
            "foo": randint(0, 100),
            "bar": {
                "baz": fake.name(),
                "poo": float(random.randrange(155, 389)) / 100,
            },
        }
        return my_dict

    @task()
    def repeat(rnd_json: dict) -> List[dict]:
        return [rnd_json, rnd_json]

    @task()
    def log(rnd_array: List[dict]):
        print("New Array: ")
        print(rnd_array)

    rndJson = generate()
    rndArray = repeat(rndJson)
    log(rndArray)


iotoi_first_workflow = test_1()