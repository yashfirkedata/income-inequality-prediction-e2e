
import pandas as pd
import numpy as np
import os
import sys
from src.IncomeInequalityPrediction.logger import logging
from src.IncomeInequalityPrediction.exception import customexception
from dataclasses import dataclass
from src.IncomeInequalityPrediction.utils.utils import save_object, evaluate_model

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import xgboost as xgb



@dataclass 
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')
    
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initate_model_training(self,train_array,test_array):
        try:
            logging.info('Splitting Dependent and Independent variables from train and test data')

            # Assuming 'income_above_limit' is the last column in your array
            X_train = train_array[:, :-1]  # All columns except the last one
            y_train = train_array[:, -1]   # Last column (income_above_limit) as target variable

            X_test = test_array[:, :-1]    # All columns except the last one
            y_test = test_array[:, -1]     # Last column (income_above_limit) as target variable

            logging.info('Model Training Started')
            models={
            'XGBoost':xgb.XGBClassifier(),
            'RandomForest':RandomForestClassifier(),
            'DecisionTree':DecisionTreeClassifier()
        }
            
            model_report:dict=evaluate_model(X_train,y_train,X_test,y_test,models)
            print(model_report)
            print('\n====================================================================================\n')
            logging.info(f'Model Report : {model_report}')

            # To get best model score from dictionary 
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            
            best_model = models[best_model_name]

            print(f'Best Model Found , Model Name : {best_model_name} , Accuracy Score : {best_model_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name} , Accuracy Score : {best_model_score}')

            save_object(
                 file_path=self.model_trainer_config.trained_model_file_path,
                 obj=best_model
            )
          

        except Exception as e:
            logging.info('Exception occured at Model Training')
            raise customexception(e,sys)

        
    