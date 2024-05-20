
import os
import sys
import pandas as pd
import numpy as np

from dataclasses import dataclass
from src.IncomeInequalityPrediction.logger import logging
from src.IncomeInequalityPrediction.exception import customexception

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, RobustScaler
from imblearn.over_sampling import SMOTE

from src.IncomeInequalityPrediction.utils.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

        
    
    def get_data_transformation(self):
        
        try:
            logging.info('Data Transformation initiated')
            
            # Define which columns should be onehot-encoded and which should be scaled
            categorical_cols = ['gender', 'education', 'marital_status', 'race', 'is_hispanic',
                'employment_commitment', 'industry_code_main', 'household_summary',
                'tax_status', 'citizenship']
            numerical_cols = ['age', 'employment_stat', 'wage_per_hour', 'working_week_per_year',
                'industry_code', 'occupation_code', 'total_employed', 'vet_benefit',
                'gains', 'losses', 'stocks_status', 'mig_year', 'importance_of_record']

            
            logging.info('Pipeline Initiated')
            
            ## Numerical Pipeline
            num_pipeline=Pipeline(
                steps=[
                    ('scaler', RobustScaler())
                ]
            )
            
            # Categorigal Pipeline
            cat_pipeline=Pipeline(
                steps=[
                ('onehot',OneHotEncoder(sparse_output=False))
                ('scaler',RobustScaler())
                ]

            )
            
            preprocessor=ColumnTransformer([
            ('num_pipeline',num_pipeline,numerical_cols),
            ('cat_pipeline',cat_pipeline,categorical_cols)
            ])
            
            return preprocessor
            

            
            
        
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")

            raise customexception(e,sys)
            
    
    def initialize_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            
            logging.info("read train and test data complete")
            logging.info(f'Train Dataframe Head : \n{train_df.head().to_string()}')
            logging.info(f'Test Dataframe Head : \n{test_df.head().to_string()}')
            
            preprocessing_obj = self.get_data_transformation()
            
            target_column_name = 'income_above_limit'
            cols_to_drop = ['id', 'class', 'education_institute', 'unemployment_reason', 'is_labor_union', 
                            'occupation_code_main', 'under_18_family', 'veterans_admin_questionnaire', 
                            'residence_1_year_ago', 'old_residence_reg', 'old_residence_state',
                            "migration_code_change_in_msa","migration_prev_sunbelt","migration_code_move_within_reg",
                            "migration_code_change_in_reg", 'country_of_birth_own','country_of_birth_father','country_of_birth_mother',
                            'household_stat']
            drop_columns = [target_column_name, cols_to_drop]
            
            input_feature_train_df = train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df=train_df[target_column_name]
            
            
            input_feature_test_df=test_df.drop(columns=drop_columns,axis=1)
            target_feature_test_df=test_df[target_column_name]
            
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)
            
            logging.info("Applying preprocessing object on training and testing datasets.")

            smote = SMOTE(random_state=42)
            input_feature_train_arr, target_feature_train_df = smote.fit_resample(input_feature_train_arr, target_feature_train_df)

            logging.info("Resampling of the data completed using SMOTE.")
            
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            
            logging.info("preprocessing pickle file saved")
            
            return (
                train_arr,
                test_arr
            )
            
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")

            raise customexception(e,sys)
            
    