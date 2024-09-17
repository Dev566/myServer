from flask import Blueprint
from flask import flash
from flask import request
import json
import requests

bp = Blueprint("page", __name__, url_prefix='/waku')

def fetch_webpage_content(url: str) -> str:
    try:
        # Send an HTTP request to the given URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:

            return response.text
        else:
            return f"Failed to fetch the page. Status code: {response.status_code}"

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
    
    
@bp.route('/download', methods=['POST'])
def video_analysis():
    url = request.json['url']
    fetch_webpage_content(url)
    locations_set = fetch_webpage_content(url)
    data = {}
    data['content'] = locations_set
    data['status'] = "200"
    return data