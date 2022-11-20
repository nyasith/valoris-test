from __main__ import app
from flask import Flask, jsonify, request, make_response
import controller.loan as controller

@app.route("/api/view-loan_details", methods=["GET"])
def getloandetails():
    res = controller.getloandetails(nric)
    return res

@app.route("/api/createloan", methods=["POST"])
def createloan():
    data = request.get_json(force=True)
    print(data)
    res = controller.createloan(data)
    return res

@app.route("/api/loanCR_master", methods=["POST"])
def insertloanCR_master():
    data = request.get_json(force=True)
    print(data)
    res = controller.insert_loanCR_master(data)
    return res

