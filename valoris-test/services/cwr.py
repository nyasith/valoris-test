import random
from db import get_db
from flask import jsonify, make_response

def createcwr(status_date,loan_amt,loan_type,balance_amount,risk_type, risk_level,job_title,employment_date,employer,email_status,name,qualification,nric,gender,phone_status):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM cwr WHERE nric = ?"
    cursor.execute(statement, [nric])
    data = cursor.fetchall()
    r_data = list(data[0])
    r_metadata = list(())
    return make_response(jsonify({"message": "Sucessfully retreived!", "error": '0', "data": r_data, "meta": r_metadata}), 200)


def insert_user(status_date,loan_amt,loan_type,balance_amount,risk_type, risk_level,job_title,employment_date,employer,email_status,name,qualification,nric,gender,phone_status):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM cwr WHERE nric = ?"
    cursor.execute(statement, [nric])
    data = cursor.fetchall()
    if len(data) > 0:
        return make_response(jsonify({"message": "data already exists", "user": {"nric": nric}, "error": "1", "meta": None}), 409)
    statement = "INSERT INTO login (status_date,loan_amt,loan_type,balance_amount,risk_type, risk_level,job_title,employment_date,employer,email_status,name,qualification,nric,gender,phone_status) VALUES (?, ?, ?, ?,?, ?, ?, ?,?, ?, ?, ?,?, ?, ?)"
    cursor.execute(statement, [status_date,loan_amt,loan_type,balance_amount,risk_type, risk_level,job_title,employment_date,employer,email_status,name,qualification,nric,gender,phone_status])
    db.commit()
    statement = "INSERT INTO user_contact (nric, phone, email, status, otp, record_date) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [status_date,loan_amt,loan_type,balance_amount,risk_type, risk_level,job_title,employment_date,employer,email_status,name,qualification,nric,gender,phone_status])
    db.commit()
    #send_email(otp, email)
    return make_response(jsonify({"message": "User successfully created. Waiting for verification", "data": nric, "error": "0", "meta": None}), 200)
