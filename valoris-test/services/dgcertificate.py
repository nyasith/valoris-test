import random
from db import get_db
from flask import jsonify, make_response

def insertdgcertificate(nric):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT course,dc_id FROM digital_certificate WHERE nric = ?"
    cursor.execute(statement, [nric])
    data = cursor.fetchall()
    r_data = list(data)
    r_metadata = list(())
    if not r_data:
        return make_response(jsonify({"message": "No Recodes", "error": '1', "data": r_data, "meta": r_metadata}), 200)
    return make_response(jsonify({"message": "Sucessfully retreived!", "error": '0', "data": r_data, "meta": r_metadata}), 200)


def getcertificate(dc_id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM digital_certificate WHERE dc_id = ?"
    cursor.execute(statement, [dc_id])
    data = cursor.fetchall()
    r_data = list(data[0])
    r_metadata = list(())
    return make_response(jsonify({"message": "Sucessfully retreived!", "error": '0', "data": r_data, "meta": r_metadata}), 200)

def getcerti(nric):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM digital_certificate WHERE nric = ?"
    cursor.execute(statement, [nric])
    data = cursor.fetchall()
    r_data = list(data[0])
    r_metadata = list(())
    return make_response(jsonify({"message": "Sucessfully retreived!", "error": '0', "data": r_data, "meta": r_metadata}), 200)
