from __main__ import app
from flask import Flask, jsonify, request, make_response
import controller.cwr as controller


@app.route("/api/cwr", methods=["POST"])
def createcwr():
    data = request.get_json(force=True)
    print(data)
    res = controller.createcwr(data)
    return res




    