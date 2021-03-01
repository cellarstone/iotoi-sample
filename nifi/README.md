


# RUN

`docker-compose up`

# PERMISSIONS

Create folder `container-data`.

Create folder `nifi_lib`.

Download PostgreSql library for Nifi: 

```shell
cd lib 
wget https://jdbc.postgresql.org/download/postgresql-42.2.18.jar
```

Set permissions for shared volume folders

`sudo chmod 777 registry`
`sudo chmod 777 nifi_lib`


