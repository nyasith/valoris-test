import random
from db import get_db
from flask import jsonify, make_response

def insert_user(nric, phone, email, password, otp, record_date):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM login WHERE nric = ?"
    cursor.execute(statement, [nric])
    data = cursor.fetchall()
    if len(data) > 0:
        return make_response(jsonify({"message": "User already exists", "user": {"nric": nric}, "error": "1", "meta": None}), 409)
    statement = "INSERT INTO login (nric, password, status, record_date) VALUES (?, ?, ?, ?)"
    cursor.execute(statement, [nric, password, '0', record_date])
    db.commit()
    statement = "INSERT INTO user_contact (nric, phone, email, status, otp, record_date) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [nric, phone, email, '0', otp, record_date])
    db.commit()
    #send_email(otp, email)
    return make_response(jsonify({"message": "User successfully created. Waiting for verification", "data": nric, "error": "0", "meta": None}), 200)


def create_user(nric, phone, email, password, otp, record_date):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM login WHERE nric = ?"
    cursor.execute(statement, [nric])
    data = cursor.fetchall()
    if len(data) > 0:
        return make_response(jsonify({"message": "User already exists", "user": {"nric": nric}, "error": "1", "meta": None}), 409)
    statement = "INSERT INTO login (nric, password, status, record_date) VALUES (?, ?, ?, ?)"
    cursor.execute(statement, [nric, password, '1', record_date])
    db.commit()
    statement = "INSERT INTO user_contact (nric, phone, email, status, otp, record_date) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [nric, phone, email, '0',  otp, record_date])
    db.commit()
    # send_email(qrcode, email)
    return make_response(jsonify({"message": "User successfully created. Waiting for verification", "data": nric, "error": "0", "meta": None}), 200)

