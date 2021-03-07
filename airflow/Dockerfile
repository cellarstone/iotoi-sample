FROM apache/airflow:2.0.1

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install faker
RUN pip install 'apache-airflow[sendgrid]'
RUN pip install apache-airflow-providers-amazon
RUN pip install clickhouse_driver
# RUN pip install airflow-clickhouse-plugin
RUN pip install kafka-python