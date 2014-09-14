from app import app
from app.models import testimonial
from flask import abort, jsonify
import json


@app.route('/plo/testimonials', methods = ['GET'])
def get_all_testimonials():
    entities = testimonial.Testimonial.query.all()
    return json.dumps([entity.to_dict() for entity in entities])


@app.route('/plo/testimonials/<int:id>', methods = ['GET'])
def get_testimonial(id):
    entity = testimonial.Testimonial.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())
