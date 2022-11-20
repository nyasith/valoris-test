import services.cwr as service

def createcwr(data):
    name =data['name']
    nric = data['nric']
    qualification = data['qualification']
    gender = data['gender']
    phone_status = data['phone_status']
    email_status = data['email_status']
    employer = data['employer']
    employment_date = data['employment_date']
    job_title = data['job_title']
    risk_level = data['risk_level']
    risk_type =data['risk_type']
    balance_amount = data['balance_amount']
    loan_type = data['loan_type']
    loan_amt = data['loan_amt']
    status_date= data['status_date']
    res = service.createcwr(status_date,loan_amt,loan_type,balance_amount,risk_type, risk_level,job_title,employment_date,employer,email_status,name,qualification,nric,gender,phone_status )
    return res

