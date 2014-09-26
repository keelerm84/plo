from app import app
from app.models import resource
import json


@app.route('/plo/resources', methods=['GET'])
def get_all_resources():
    entities = resource.Resource.query.all()
    return json.dumps([entity.to_dict() for entity in entities])
