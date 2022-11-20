from functools import wraps
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
import pytz
import datetime as dt
from unittest import result
import sys

sys.dont_write_bytecode = True

kuala_lumpur = pytz.timezone('Asia/Kuala_Lumpur')
now = dt.datetime.now()
now_in_kuala_lumpur = now.astimezone(kuala_lumpur)

app = Flask(__name__)
CORS(app)

import routes.up
import routes.auth
import routes.cwr
import routes.dgcertificate
import routes.loan
import routes.profile


@app.after_request
def after_request(response):
    # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response


if __name__ == "__main__":
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
