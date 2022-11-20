
from __main__ import app
from flask import Flask, jsonify, request, make_response

@app.route("/api/up", methods=["GET"])
def up():
    return jsonify({"message": "1.0 is Up and Running!", "data": None, "error": "0", "meta": None})

