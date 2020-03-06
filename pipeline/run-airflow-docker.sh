#!/bin/sh
export APP_HOME="$(cd "`dirname "$0"`"/..; pwd)"

docker run --rm \
           --name airfllow-demo \
           -u root \
           -p 8080:8080 \
           -v "${APP_HOME}"/pipeline/dags/:/usr/local/airflow/dags \
           -v "${APP_HOME}"/src:/src \
           puckel/docker-airflow webserver