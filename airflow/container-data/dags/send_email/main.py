from typing import Any, Dict

import requests

from airflow.decorators import dag, task
from airflow.models.baseoperator import BaseOperator
from airflow.operators.email import EmailOperator
from airflow.utils.dates import days_ago

DEFAULT_ARGS = {"owner": "iotoi"}


class GetRequestOperator(BaseOperator):
    """Custom operator to sand GET request to provided url"""

    def __init__(self, *, url: str, **kwargs):
        super().__init__(**kwargs)
        self.url = url

    def execute(self, context):
        return requests.get(self.url).json()


# [START dag_decorator_usage]
@dag(
    default_args=DEFAULT_ARGS,
    schedule_interval=None,
    start_date=days_ago(2),
    tags=["iotoi-samples"],
)
def send_email(email: str = "lukas.kellerstein@gmail.com"):
    """
    DAG to send server IP to email.

    :param email: Email to send IP to. Defaults to example@example.com.
    :type email: str
    """
    get_ip = GetRequestOperator(task_id="get_ip", url="http://httpbin.org/get")

    @task(multiple_outputs=True)
    def prepare_email(raw_json: Dict[str, Any]) -> Dict[str, str]:
        external_ip = raw_json["origin"]
        return {
            "subject": f"Hello from the Apache Aiflow",
            "body": f"This email is send by IoToI workflow.<br>Seems like today your server executing Airflow is connected from IP {external_ip}<br>",
        }

    email_info = prepare_email(get_ip.output)

    EmailOperator(
        task_id="send_email",
        to=email,
        subject=email_info["subject"],
        html_content=email_info["body"],
    )


dag = send_email()
# [END dag_decorator_usage]