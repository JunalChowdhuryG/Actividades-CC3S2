FROM apache/airflow:2.9.1-python3.11

USER root
COPY airflow/dags /opt/airflow/dags
COPY ../app /app  

USER airflow

ARG AIRFLOW_VERSION=2.9.1
ARG PYTHON_VERSION=3.11
ARG CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

RUN pip install --no-cache-dir \
    --constraint "${CONSTRAINT_URL}" \
    pandas psycopg2-binary