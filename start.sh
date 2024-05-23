#!bin/sh
nohup airflow scheduler &
airflow webserver

!/bin/sh

# # Wait for Airflow initialization
# echo "Waiting for Airflow initialization..."
# until airflow db check; do
#   >&2 echo "Airflow is unavailable - sleeping"
#   sleep 1
# done

# echo "Airflow is initialized. Starting Airflow services..."
# # Start Airflow webserver and scheduler
# airflow webserver --port 8080 &
# airflow scheduler
