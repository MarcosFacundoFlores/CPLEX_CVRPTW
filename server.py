from flask import Flask, jsonify, request
from flask_cors import CORS
from flask import render_template

app = Flask(__name__,
            )
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def render_vue(path):
    return render_template("index.html")


MOCK_SOLUTION = {
    "routes": [
        {"vehicle": 1, "locations": [1, 2, 3]},
        {"vehicle": 2, "locations": [4, 5, 6]}
    ],
    "total_distance": 100
}

@app.route('/api/cvrptw', methods=['POST'])
def solve_cvrptw():

    data = request.get_json()

    solution = MOCK_SOLUTION

    return jsonify(solution)

if __name__ == '__main__':
    app.run(debug=True)
