
# RUN:

`docker build -t apache/airflow:2.0.1 .`

`docker-compose up airflow-init`

then

`docker-compose up`

open

`http://localhost:8080`

```
login: airflow
password: airflow
```