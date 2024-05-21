    
from src.IncomeInequalityPrediction.pipelines.prediction_pipeline import CustomData,PredictPipeline

from flask import Flask,request,render_template,jsonify


app=Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html")


@app.route("/predict",methods=["GET","POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("index.html")
    
    else:
        data=CustomData(
            ID=request.form.get('ID'),
            age=int(request.form.get('age')),
            gender=request.form.get('gender'),
            education=request.form.get('education'),
            class_name=request.form.get('class'),
            education_institute=request.form.get('education_institute'),
            marital_status=request.form.get('marital_status'),
            race=request.form.get('race'),
            is_hispanic=request.form.get('is_hispanic'),
            employment_commitment=request.form.get('employment_commitment'),
            unemployment_reason=request.form.get('unemployment_reason'),
            employment_stat=int(request.form.get('employment_stat')),
            wage_per_hour=int(request.form.get('wage_per_hour')),
            is_labor_union=request.form.get('is_labor_union'),
            working_week_per_year=int(request.form.get('working_week_per_year')),
            industry_code=int(request.form.get('industry_code')),
            industry_code_main=request.form.get('industry_code_main'),
            occupation_code=int(request.form.get('occupation_code')),
            occupation_code_main=request.form.get('occupation_code_main'),
            total_employed=int(request.form.get('total_employed')),
            household_stat=request.form.get('household_stat'),
            household_summary=request.form.get('household_summary'),
            under_18_family=request.form.get('under_18_family'),
            veterans_admin_questionnaire=request.form.get('veterans_admin_questionnaire'),
            vet_benefit=int(request.form.get('vet_benefit')),
            tax_status=request.form.get('tax_status'),
            gains=int(request.form.get('gains')),
            losses=int(request.form.get('losses')),
            stocks_status=int(request.form.get('stocks_status')),
            citizenship=request.form.get('citizenship'),
            mig_year=int(request.form.get('mig_year')),
            country_of_birth_own=request.form.get('country_of_birth_own'),
            country_of_birth_father=request.form.get('country_of_birth_father'),
            country_of_birth_mother=request.form.get('country_of_birth_mother'),
            migration_code_change_in_msa=request.form.get('migration_code_change_in_msa'),
            migration_prev_sunbelt=request.form.get('migration_prev_sunbelt'),
            migration_code_move_within_reg=request.form.get('migration_code_move_within_reg'),
            migration_code_change_in_reg=request.form.get('migration_code_change_in_reg'),
            residence_1_year_ago=request.form.get('residence_1_year_ago'),
            old_residence_reg=request.form.get('old_residence_reg'),
            old_residence_state=request.form.get('old_residence_state'),
            importance_of_record=float(request.form.get('importance_of_record'))
        )
        # this is my final data
        final_data=data.get_data_as_dataframe()
        
        predict_pipeline=PredictPipeline()
        
        pred=predict_pipeline.predict(final_data)
        
        result= pred
        
        return render_template("result.html",final_result=result)

#execution begin
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)