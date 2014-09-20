from app import app
from app.models import doctor
import json


@app.route('/plo/doctors', methods = ['GET'])
def get_all_doctors():
    entities = doctor.Doctor.query.all()
    return json.dumps([entity.to_dict() for entity in entities])
