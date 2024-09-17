from flask import Blueprint
from flask import flash
import json


bp = Blueprint("healthCheck", __name__, url_prefix='/waku')

@bp.route('/healthCheck', methods=['GET'])
def health_check():
  data = {}
  data['name'] = "Vivy"
  data['description'] = "Vivy is running"
  return json.dumps(data)


@bp.route('/healthCheckPost', methods=['POST'])
def health_check_post():
  data = {}
  data['name'] = "Vivy"
  data['description'] = "Vivy is running"
  return json.dumps(data)