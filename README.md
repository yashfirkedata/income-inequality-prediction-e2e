# Gemstone Price Prediction

## Description
```
Getting a rapid understanding of the context of a patient’s overall health has been particularly important during the COVID-19 pandemic as healthcare workers around the world struggle with hospitals overloaded by patients in critical condition. Intensive Care Units (ICUs) often lack verified medical histories for incoming patients. A patient in distress or a patient who is brought in confused or unresponsive may not be able to provide information about chronic conditions such as heart disease, injuries, or diabetes. Medical records may take days to transfer, especially for a patient from another medical provider or system. Knowledge about chronic conditions can inform clinical decisions about patient care and ultimately improve patient's survival outcomes.
```

## Problem Statement

```The target feature is hospital_death which is a binary variable. The task is to classify this variable based on the other 84 features step-by-step by going through each day's task. The scoring metric is Accuracy/Area under ROC curve.```

## Project setup:


### Clone repository
```bash
git clone https://github.com/yashfirkedata/income-inequality-prediction-e2e.git
```

### Setup development environment
```bash
bash init_setup.sh
```
```bash
python setup.py install
```

### Acivate environment
```bash
source activate ./venv
```

### Start Docker Container
```bash
docker-compose up
```

### Start Airflow schedular and Flask app
**Airflow Schedular**: localhost:8080

**Flask app**: localhost:5050

**Experiment tracking (MLFlow):**
```bash
mlflow ui 
```

## Pipelines
### Training Pipeline
    * Data Ingestion (fetched data from source)
    * Data Transformation (Feature Engineering, Data Preprocessing)
    * Model Builing (Create a model using the processed data)

## MLFlow & DagsHub
Copy the values from DagsHub > Repo > Remote > Experiments

```bash
set MLFLOW_TRACKING_URI=<>
set MLFLOW_TRACKING_USERNAME=<>
set MLFLOW_TRACKING_PASSWORD<>
```
If the above are not set, then ML Experiments gets registered in local system else gets published to DagsHub

#### Command to train the pipeline
```bash
python src\GemstonePricePrediction\pipelines\training_pipeline.py
```

### Prediction Pipeline
    * Two types of prediction pipeline
        * Single record prediction
        * Batch prediction


## Explainer Dashboard

* Feature Importance
* Regression Stats
* Individual Predictions
* What if?
* Feature Dependence

```bash
python dashboard.py
```

## Flask App
```bash
python app.py
```

## Streamlit App
```bash
streamlit run streamlit_app.py
```

## Training Experiments - DagsHub

https://dagshub.com/abhijitpaul0212/GemstonePricePrediction


## Deployment of DockerImage on AWS
* AWS - ECR
* AWS - AppRunner

## Cloud Deployed Links
* https://gemstonepriceprediction.streamlit.app/
* https://g3smncimby.us-east-1.awsapprunner.com/


## Dataset Link
* https://www.kaggle.com/datasets/colearninglounge/gemstone-price-prediction
* https://raw.githubusercontent.com/abhijitpaul0212/DataSets/main/gemstone.csv