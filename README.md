# Gemstone Price Prediction

## Description
```🏥 Getting a rapid understanding of the context of a patient’s overall health has been particularly important during the COVID-19 pandemic as healthcare workers around the world struggle with hospitals overloaded by patients in critical condition. Intensive Care Units (ICUs) often lack verified medical histories for incoming patients. A patient in distress or a patient who is brought in confused or unresponsive may not be able to provide information about chronic conditions such as heart disease, injuries, or diabetes. Medical records may take days to transfer, especially for a patient from another medical provider or system. Knowledge about chronic conditions can inform clinical decisions about patient care and ultimately improve patient's survival outcomes.```

## Problem Statement

```📋 The target feature is hospital_death which is a binary variable. The task is to classify this variable based on the other 84 features step-by-step by going through each day's task. The scoring metric is Accuracy/Area under ROC curve.```

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

### Start Airflow Scheduler and Flask App

**Airflow Scheduler**: [localhost:8080](http://localhost:8080) 🌐

**Flask App**: [localhost:5050](http://localhost:5050) 🚀

**Experiment Tracking (MLFlow)**:
```bash
mlflow ui

```

## Pipelines and Components

### Raw Experiments
- [Raw Experiments Notebook](notebooks/experiments_nb.ipynb) - Jupyter notebook containing raw experiments and analysis.

### Components
- [Data Ingestion Component](src/IncomeInequalityPrediction/components/data_ingestion.py) - Module for ingesting data from various sources.
- [Data Transformation Component](src/IncomeInequalityPrediction/components/data_transformation.py) - Module for transforming and cleaning the ingested data.
- [Model Evaluation Component](src/IncomeInequalityPrediction/components/model_evaluation.py) - Module for evaluating the performance of the trained model.
- [Model Trainer Component](src/IncomeInequalityPrediction/components/model_trainer.py) - Module for training the machine learning model.

### Running Pipelines
- [Training Pipeline](src/IncomeInequalityPrediction/pipelines/training_pipeline.py) - Pipeline for training the machine learning model.
- [Prediction Pipeline](src/IncomeInequalityPrediction/pipelines/prediction_pipeline.py) - Pipeline for making predictions using the trained model.

### Utils
- [Utility Functions](src/IncomeInequalityPrediction/utils/utils.py) - Utility functions used across the project.

### Logging and Exception Handling
- [Logger Module](src/IncomeInequalityPrediction/logger.py) - Module for logging messages and events.
- [Exception Module](src/IncomeInequalityPrediction/exception.py) - Module for defining custom exceptions.

## Images
### MLFLow UI

- **Function**: Displays different experiments carried out, logging various details such as model parameters, metrics, etc.
- **Data Display**: The UI presents the data present in `mlruns/0` folder in a user-friendly format.

![MLFlow UI](https://github.com/yashfirkedata/income-inequality-prediction-e2e/blob/f4e3b5ed8809f6f3f72ed9922f7dfba124417be4/images/mlflow.jpg)

### Flask Application (app.py)

- **Description**: The Flask application is responsible for serving the web application for the income inequality prediction project.
  
![Flask Application](https://github.com/yashfirkedata/income-inequality-prediction-e2e/blob/f4e3b5ed8809f6f3f72ed9922f7dfba124417be4/images/app.jpg)

> Please forgive my poor html css skills 🙂

---

### Airflow Scheduler UI

- **Description**: The Airflow Scheduler UI provides a graphical interface to manage and monitor workflows in the income inequality prediction project.
  
![Airflow Scheduler UI](https://github.com/yashfirkedata/income-inequality-prediction-e2e/blob/f4e3b5ed8809f6f3f72ed9922f7dfba124417be4/images/screen.jpg)

---

---

# Thank You! 🙏

Thank you for checking out this project. Your support, any Contribution and feedback are greatly appreciated! 😊

    
