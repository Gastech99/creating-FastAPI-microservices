from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/greet", methods=['GET'])
def greet():
    return jsonify(message="Hello, Welcome")


@app.route('/submit', methods=['POST'])
def submit():
    data = request.json  # Get the JSON from the request
    name = data.get('name')  # Extract the name field from the JSON
    if name:  # Basic validation
        return jsonify(message="Hello, {name}!")
    return jsonify(error="No name provided"), 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
