import services.dgcertificate as service
from db import get_db
from flask import jsonify, make_response


def insertdgcertificate(data):
    dept_name = data['dept_name'],
    ministry = data['ministry'],
    cert_title = data["cert_title"],
    course = data["course"],
    level = data["level"],
    name = data["name"],
    nric = data["nric"],
    college_name = data[' college_name']
    state = data['state']
    cert_no1 = data['cert_no1']
    cert_no2 = data['cert_no2']
    generated_date = data['generated_date']
    status = data['status']
    
    res = service.insertdgcertificate(dept_name,ministry,cert_title,course,level,name,nric, college_name,state,cert_no1,
    cert_no2,generated_date,status)
    return res



def getcertificate(dc_id):
    res = service.getcertificate(dc_id)
    return res

def getcerti(nric):
    res = service.getcerti(nric)
    return res