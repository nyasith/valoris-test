from __main__ import app
import profile
from flask import Flask, jsonify, request, make_response
import controller.profile as controller

#@app.route('/api/login', methods=['POST'])
#def createloan():
   # data = request.get_json(force=True)
   # print(data)
  #  res = controller.createloann(data)
  #  return res

