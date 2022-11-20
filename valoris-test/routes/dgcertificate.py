from __main__ import app
from flask import Flask, jsonify, request, make_response
import controller.dgcertificate as controller

@app.route("/api/dgcertificate", methods=["POST"])
def insertdgcertificate():
    data = request.get_json(force=True)
    print(data)
    res = controller.insertdgcertificate(data)
    return res


@app.route("/api/createdgcertificate/", methods=["GET"])
def getcerti():
    nric = request.args.get('nric', None)
    result = controller.getcerti(nric)
    return result


@app.route("/api/digital-certificate/", methods=["GET"])
def get_certificate():
    dc_id = request.args.get('dc_id', None)
    result = controller.getcertificate(dc_id)
    return result
