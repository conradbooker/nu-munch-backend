import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load data from JSON files
def load_data(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

users = load_data('users.json')
eateries = load_data('eateries.json')
orders = load_data('orders.json')

# Save data back to JSON files (if needed, e.g., for updates)
def save_data(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

# GET request to retrieve user information
@app.route('/users/<user_id>', methods=['GET','POST'])
def get_user(user_id):
    if request.method == "GET":
        user = users.get(str(user_id))  # Use string key for JSON compatibility
        if user:
            return jsonify(user)
        return jsonify({"error": "User not found"}), 404

# POST request to add user information
@app.route('/users', methods=['POST'])
def add_user():
    if request.method == "POST":
        new_user = request.json  # Get the data from the POST request
        user_id = str(new_user.get("id"))  # Assume "id" is part of the data
        if user_id in users:
            return jsonify({"error": "User already exists"}), 400
        users[user_id] = new_user
        save_data(users, 'users.json')  # Save changes to the file
        return jsonify({"message": "User added successfully"}), 201

# GET request to retrieve eatery information
@app.route('/eateries/<eatery_id>', methods=['GET','POST'])
def get_eatery(eatery_id):
    if request.method == "GET":
        eatery = eateries.get(str(eatery_id))  # Use string key for JSON compatibility
        if eatery:
            return jsonify(eatery)
        return jsonify({"error": "Eatery not found"}), 404

# POST request to add eatery information
@app.route('/eateries', methods=['POST'])
def add_eatery():
    if request.method == "POST":
        new_eatery = request.json  # Get the data from the POST request
        eatery_id = str(new_eatery.get("id"))  # Assume "id" is part of the data
        if eatery_id in eateries:
            return jsonify({"error": "Eatery already exists"}), 400
        eateries[eatery_id] = new_eatery
        save_data(eateries, 'eateries.json')  # Save changes to the file
        return jsonify({"message": "Eatery added successfully"}), 201
    
# GET request to retrieve order information
@app.route('/orders/<order_id>', methods=['GET','POST'])
def get_order(order_id):
    if request.method == "GET":
        order = orders.get(str(order_id))  # Use string key for JSON compatibility
        if order:
            return jsonify(order)
        return jsonify({"error": "Order not found"}), 404

# POST request to add order information
@app.route('/orders', methods=['POST'])
def add_order(order_id):
    if request.method == "POST":
        new_order = request.json  # Get the data from the POST request
        order_id = str(new_order.get("id"))  # Assume "id" is part of the data
        if order_id in orders:
            return jsonify({"error": "Order already exists"}), 400
        orders[order_id] = new_order
        save_data(orders, 'orders.json')  # Save changes to the file
        return jsonify({"message": "Order added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)