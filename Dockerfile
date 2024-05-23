FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app

RUN apt update -y

RUN apt-get update && pip install -r requirements.txt
CMD ["python3", "app.py"]

# FROM python:3.8-slim-buster
# USER root
# RUN mkdir /app
# COPY . /app/
# WORKDIR /app/
# RUN pip3 install -r requirements.txt
# ENV AIRFLOW_HOME="/app/airflow"
# ENV AIRFLOW_CORE_DAGBAG_IMPORT_TIMEOUT=1000
# ENV AIRFLOW_CORE_ENABLE_XCOM_PICKLING=True
# RUN airflow db init
# RUN airflow users create -e yashfirke.edu@gmail.com -f yash -l firke -p admin -r Admin -u admin
# RUN chmod 777 start.sh
# RUN apt update -y
# ENTRYPOINT [ "/bin/sh" ]
# CMD ["start.sh"]