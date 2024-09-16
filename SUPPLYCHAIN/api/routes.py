from flask import Blueprint, request, jsonify
from .models import optimize_routes

api_bp = Blueprint('api', __name__)

@api_bp.route('/optimize', methods=['POST'])
def optimize():
    data = request.get_json()
    # Extract user inputs from the request
    cost_per_route = data['cost_per_route']
    time_per_route = data['time_per_route']
    max_time = data['max_time']

    # Call the optimization function
    result = optimize_routes(cost_per_route, time_per_route, max_time)

    return jsonify(result)
