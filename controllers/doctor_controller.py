from flask import request, jsonify, make_response
from datetime import datetime

from models.doctor_model import Doctor
items = []
def create_doctor():
    data = request.get_json()

    try:
        doctor = Doctor(**data)
    except ValueError as e:
        jsonify({"error": str(e)}), 400

    items.append(data)
    return make_response('', 201)

