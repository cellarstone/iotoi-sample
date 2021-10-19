FROM apache/airflow:2.0.1
USER root
RUN apt-get update && apt-get install -y default-jdk && apt-get clean
USER airflow
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install faker
RUN pip install requests
RUN pip install 'apache-airflow[sendgrid]'
RUN pip install apache-airflow-providers-amazon
RUN pip install apache-airflow-providers-apache-spark
RUN pip install clickhouse_driver
# RUN pip install airflow-clickhouse-plugin
RUN pip install kafka-python
