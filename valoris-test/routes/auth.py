from __main__ import app
from flask import Flask, jsonify, request, make_response
import controller.auth as controller

@app.route("/api/user-create", methods=["POST"])
def create_user():
    data = request.get_json(force=True)
    print(data)
    res = controller.create_user(data)
    return res

@app.route("/api/user-insert", methods=["POST"])
def insert_user():
    data = request.get_json(force=True)
    print(data)
    res = controller.insert_user(data)
    return res