import os
import sys
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import pickle
from src.IncomeInequalityPrediction.logger import logging
from src.IncomeInequalityPrediction.exception import customexception
from src.IncomeInequalityPrediction.utils.utils import save_object, load_object


class ModelEvaluation:
    def __init__(self):
        pass

    
    def eval_metrics(self, actual, pred):
        accuracy = accuracy_score(actual, pred)
        precision = precision_score(actual, pred)
        recall = recall_score(actual, pred)
        f1 = f1_score(actual, pred)
        roc_auc = roc_auc_score(actual, pred)
        logging.info("metrics calculated")
        return accuracy, precision, recall, f1, roc_auc


    def initiate_model_evaluation(self,train_array,test_array):
        try:
            X_test,y_test=(test_array[:,:-1], test_array[:,-1])

            model_path=os.path.join("artifacts","model.pkl")
            model=load_object(model_path)

        

            #mlflow.set_registry_uri("")

            logging.info("model has registered")
            
            tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
            
            print(tracking_url_type_store)


            logging.info('Model Evaluation Started - run started with MLFlow')
            with mlflow.start_run():

                predicted_qualities = model.predict(X_test)

                (accuracy, precision, recall, f1, roc_auc) = self.eval_metrics(y_test, predicted_qualities)

                mlflow.log_metric("accuracy", accuracy)
                mlflow.log_metric("precision", precision)
                mlflow.log_metric("recall", recall)
                mlflow.log_metric("f1", f1)
                mlflow.log_metric("roc_auc", roc_auc)


                # this condition is for the dagshub
                # Model registry does not work with file store
                # if you set cloud location in the mlflow.set_registry_uri() then you wont get file in tracking_url_type_store therefore the condition is set.
                # if you set file location in the mlflow.set_registry_uri() then it will not work
                if tracking_url_type_store != "file":

                    # Register the model
                    # There are other ways to use the Model Registry, which depends on the use case,
                    # please refer to the doc for more information:
                    # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                    mlflow.sklearn.log_model(model, "model", registered_model_name="ml_model")
                # it is for the local 
                else:
                    mlflow.sklearn.log_model(model, "model")


                

            
        except Exception as e:
            raise e