#This method substitues the variables in the data set file with actual values for understanding purpose. The description is obtained from (https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.doc)
import numpy as np

def substitute(df):
    headers=["Status of existing checking account","Duration in month","Credit history","Purpose","Credit amount","Savings account/bonds","Present employment since","Installment rate in percentage of disposable income","Personal status and sex","Other debtors / guarantors","Present residence since","Property","Age in years","Other installment plans","Housing","Number of existing credits at this bank","Job","Number of people being liable to provide maintenance for","Telephone","foreign worker"]
    df.columns=headers
    # df.to_csv("german_data_credit_cat.csv",index=False) #save as csv file

    #for structuring only
    Status_of_existing_checking_account={'A14':"no checking account",'A11':"<0 DM", 'A12': "0 <= <200 DM",'A13':">= 200 DM "}
    Status_of_existing_checking_account = {y:x for x,y in Status_of_existing_checking_account.items()}
    df["Status of existing checking account"]=df["Status of existing checking account"].map(Status_of_existing_checking_account)

    Credit_history={"A34":"critical account","A33":"delay in paying off","A32":"existing credits paid back duly till now","A31":"all credits at this bank paid back duly","A30":"no credits taken"}
    Credit_history = {y:x for x,y in Credit_history.items()}
    df["Credit history"]=df["Credit history"].map(Credit_history)

    Purpose={"A40" : "car (new)", "A41" : "car (used)", "A42" : "furniture/equipment", "A43" :"radio/television" , "A44" : "domestic appliances", "A45" : "repairs", "A46" : "education", 'A47' : 'vacation','A48' : 'retraining','A49' : 'business','A410' : 'others'}
    Purpose = {y:x for x,y in Purpose.items()}
    df["Purpose"]=df["Purpose"].map(Purpose)

    Saving_account={"A65" : "no savings account","A61" :"<100 DM","A62" : "100 <= <500 DM","A63" :"500 <= < 1000 DM", "A64" :">= 1000 DM"}
    Saving_account = {y:x for x,y in Saving_account.items()}
    df["Savings account/bonds"]=df["Savings account/bonds"].map(Saving_account)

    Present_employment={'A75':">=7 years", 'A74':"4<= <7 years",  'A73':"1<= < 4 years", 'A72':"<1 years",'A71':"unemployed"}
    Present_employment = {y:x for x,y in Present_employment.items()}
    df["Present employment since"]=df["Present employment since"].map(Present_employment)

    Personal_status_and_sex={ 'A95':"female:single",'A94':"male:married/widowed",'A93':"male:single", 'A92':"female:divorced/separated/married", 'A91':"male:divorced/separated"}
    Personal_status_and_sex = {y:x for x,y in Personal_status_and_sex.items()}
    df["Personal status and sex"]=df["Personal status and sex"].map(Personal_status_and_sex)

    Other_debtors_guarantors={'A101':"none", 'A102':"co-applicant", 'A103':"guarantor"}
    Other_debtors_guarantors = {y:x for x,y in Other_debtors_guarantors.items()}
    df["Other debtors / guarantors"]=df["Other debtors / guarantors"].map(Other_debtors_guarantors)

    Property={'A121':"real estate", 'A122':"savings agreement/life insurance", 'A123':"car or other", 'A124':"unknown / no property"}
    Property = {y:x for x,y in Property.items()}
    df["Property"]=df["Property"].map(Property)

    Other_installment_plans={'A143':"none", 'A142':"store", 'A141':"bank"}
    Other_installment_plans = {y:x for x,y in Other_installment_plans.items()}
    df["Other installment plans"]=df["Other installment plans"].map(Other_installment_plans)

    Housing={'A153':"for free", 'A152':"own", 'A151':"rent"}
    Housing = {y:x for x,y in Housing.items()}
    df["Housing"]=df["Housing"].map(Housing)

    Job={'A174':"management/ highly qualified employee", 'A173':"skilled employee / official", 'A172':"unskilled - resident", 'A171':"unemployed/ unskilled  - non-resident"}
    Job = {y:x for x,y in Job.items()}
    df["Job"]=df["Job"].map(Job)

    Telephone={'A192':"yes", 'A191':"none"}
    Telephone = {y:x for x,y in Telephone.items()}
    df["Telephone"]=df["Telephone"].map(Telephone)

    foreign_worker={'A201':"yes", 'A202':"no"}
    foreign_worker = {y:x for x,y in foreign_worker.items()}
    df["foreign worker"]=df["foreign worker"].map(foreign_worker)

    # risk={1:"Good Risk", 2:"Bad Risk"}
    # risk = {y:x for x,y in risk.items()}
    # df["Cost Matrix(Risk)"]=df["Cost Matrix(Risk)"].map(risk)

    df.columns=np.arange(0,20)

    return df

