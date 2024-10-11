# Income Inequality Prediction

## Overview
```🏥 Income inequality - when income is distributed in an uneven manner among a population, is a growing problem in developing nations across the world. With the rapid rise of AI and worker automation, this problem could continue to grow if steps are not taken to address the issue. This solution can potentially reduce the cost and improve the accuracy of monitoring key population indicators such as income level in between census years. This information will help policymakers to better manage and avoid income inequality globally```

## Problem Statement

```📋The central problem in this project is binary classification, specifically predicting whether an individual's income is above or below a certain predefined threshold. The target feature for this classification task is "income_above_limit." The project aims to build a machine learning model that can make these income predictions effectively. The evaluation metric chosen for assessing the model's performance is the F1-score, which is a balanced measure that takes both precision and recall into account. Achieving a high F1-score indicates that the model can make accurate predictions while minimizing false positives and false negatives..```

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

    
