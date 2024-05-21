import os
import sys
import pandas as pd
import numpy as np
from src.IncomeInequalityPrediction.logger import logging
from src.IncomeInequalityPrediction.exception import customexception
from src.IncomeInequalityPrediction.utils.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self,features):
        try:
            preprocessor_path=os.path.join("artifacts","preprocessor.pkl")
            model_path=os.path.join("artifacts","model.pkl")
            
            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            # Drop unnecessary columns if any
            cols_to_drop = ['ID', 'class_name', 'education_institute', 'unemployment_reason', 'is_labor_union', 
                            'occupation_code_main', 'under_18_family', 'veterans_admin_questionnaire', 
                            'residence_1_year_ago', 'old_residence_reg', 'old_residence_state',
                            "migration_code_change_in_msa","migration_prev_sunbelt","migration_code_move_within_reg",
                            "migration_code_change_in_reg", 'country_of_birth_own','country_of_birth_father','country_of_birth_mother',
                            'household_stat']
            
            drop_columns = cols_to_drop
            features.replace('?',np.nan,inplace=True)
            
            features = features.drop(columns=drop_columns,axis=1)

            scaled_data=preprocessor.transform(features)
            
            pred=model.predict(scaled_data)
            
            # Map predicted values to corresponding labels
            prediction_labels = {0: 'Below limit', 1: 'Above limit'}
            pred_mapped = [prediction_labels[p] for p in pred]
        
            return pred_mapped
        
        except Exception as e:
            raise customexception(e,sys)
    
    
    
class CustomData:

    def __init__(self,
                 ID,
                 age,
                 gender,
                 education,
                 class_name,
                 education_institute,
                 marital_status,
                 race,
                 is_hispanic,
                 employment_commitment,
                 unemployment_reason,
                 employment_stat,
                 wage_per_hour,
                 is_labor_union,
                 working_week_per_year,
                 industry_code,
                 industry_code_main,
                 occupation_code,
                 occupation_code_main,
                 total_employed,
                 household_stat,
                 household_summary,
                 under_18_family,
                 veterans_admin_questionnaire,
                 vet_benefit,
                 tax_status,
                 gains,
                 losses,
                 stocks_status,
                 citizenship,
                 mig_year,
                 country_of_birth_own,
                 country_of_birth_father,
                 country_of_birth_mother,
                 migration_code_change_in_msa,
                 migration_prev_sunbelt,
                 migration_code_move_within_reg,
                 migration_code_change_in_reg,
                 residence_1_year_ago,
                 old_residence_reg,
                 old_residence_state,
                 importance_of_record):
        
        self.ID = ID
        self.age = age
        self.gender = gender
        self.education = education
        self.class_name = class_name
        self.education_institute = education_institute
        self.marital_status = marital_status
        self.race = race
        self.is_hispanic = is_hispanic
        self.employment_commitment = employment_commitment
        self.unemployment_reason = unemployment_reason
        self.employment_stat = employment_stat
        self.wage_per_hour = wage_per_hour
        self.is_labor_union = is_labor_union
        self.working_week_per_year = working_week_per_year
        self.industry_code = industry_code
        self.industry_code_main = industry_code_main
        self.occupation_code = occupation_code
        self.occupation_code_main = occupation_code_main
        self.total_employed = total_employed
        self.household_stat = household_stat
        self.household_summary = household_summary
        self.under_18_family = under_18_family
        self.veterans_admin_questionnaire = veterans_admin_questionnaire
        self.vet_benefit = vet_benefit
        self.tax_status = tax_status
        self.gains = gains
        self.losses = losses
        self.stocks_status = stocks_status
        self.citizenship = citizenship
        self.mig_year = mig_year
        self.country_of_birth_own = country_of_birth_own
        self.country_of_birth_father = country_of_birth_father
        self.country_of_birth_mother = country_of_birth_mother
        self.migration_code_change_in_msa = migration_code_change_in_msa
        self.migration_prev_sunbelt = migration_prev_sunbelt
        self.migration_code_move_within_reg = migration_code_move_within_reg
        self.migration_code_change_in_reg = migration_code_change_in_reg
        self.residence_1_year_ago = residence_1_year_ago
        self.old_residence_reg = old_residence_reg
        self.old_residence_state = old_residence_state
        self.importance_of_record = importance_of_record

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'ID': [self.ID],
                'age': [self.age],
                'gender': [self.gender],
                'education': [self.education],
                'class_name': [self.class_name],
                'education_institute': [self.education_institute],
                'marital_status': [self.marital_status],
                'race': [self.race],
                'is_hispanic': [self.is_hispanic],
                'employment_commitment': [self.employment_commitment],
                'unemployment_reason': [self.unemployment_reason],
                'employment_stat': [self.employment_stat],
                'wage_per_hour': [self.wage_per_hour],
                'is_labor_union': [self.is_labor_union],
                'working_week_per_year': [self.working_week_per_year],
                'industry_code': [self.industry_code],
                'industry_code_main': [self.industry_code_main],
                'occupation_code': [self.occupation_code],
                'occupation_code_main': [self.occupation_code_main],
                'total_employed': [self.total_employed],
                'household_stat': [self.household_stat],
                'household_summary': [self.household_summary],
                'under_18_family': [self.under_18_family],
                'veterans_admin_questionnaire': [self.veterans_admin_questionnaire],
                'vet_benefit': [self.vet_benefit],
                'tax_status': [self.tax_status],
                'gains': [self.gains],
                'losses': [self.losses],
                'stocks_status': [self.stocks_status],
                'citizenship': [self.citizenship],
                'mig_year': [self.mig_year],
                'country_of_birth_own': [self.country_of_birth_own],
                'country_of_birth_father': [self.country_of_birth_father],
                'country_of_birth_mother': [self.country_of_birth_mother],
                'migration_code_change_in_msa': [self.migration_code_change_in_msa],
                'migration_prev_sunbelt': [self.migration_prev_sunbelt],
                'migration_code_move_within_reg': [self.migration_code_move_within_reg],
                'migration_code_change_in_reg': [self.migration_code_change_in_reg],
                'residence_1_year_ago': [self.residence_1_year_ago],
                'old_residence_reg': [self.old_residence_reg],
                'old_residence_state': [self.old_residence_state],
                'importance_of_record': [self.importance_of_record],
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df

        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise customexception(e,sys)