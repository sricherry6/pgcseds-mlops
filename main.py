from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from utils.score import load_model, calc_risk

app = FastAPI(
    title="Cred Scoring",
    docs_url="/"
)

app.add_event_handler("startup", load_model)

class QueryIn(BaseModel):
    status_of_existing_checking_account: str = 'no checking account'
    duration_in_month: int = 10
    credit_history: str = 'critical account'
    purpose: str = 'radio/television'
    credit_amount: int = 1169
    savings_account_bonds: str = 'no savings account'
    present_employment_since: str = '>=7 years'
    installment_rate_in_percentage_of_disposable_income: int = 4
    personal_status_and_sex: str = 'male:single'
    other_debtors_guarantors: str = 'none'
    present_residence_since: int = 2
    property: str = 'real estate'
    age_in_years: int = 67
    other_installment_plans: str = 'none'
    housing: str = 'own'
    number_of_existing_credits_at_this_bank: int = 2
    job: str = 'skilled employee / official'
    number_of_people_being_liable_to_provide_maintenance_for: int = 1
    telephone: str = 'yes'
    foreign_worker: str = 'yes'

class QueryOut(BaseModel):
    risk: str


@app.get("/ping")
def ping():
    return {"ping": "pong"}


@app.post("/credit_score")
def credit_score(
    query_data: QueryIn
):
    """use ml model to calculate risk"""
    risks = {
        0: "bad risk",
        1: "good risk"
    }
    return QueryOut(**{'risk': risks[calc_risk(query_data)]})

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8888, reload=True)
