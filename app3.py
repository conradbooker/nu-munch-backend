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

users = load_data('models/users.json')
eateries = load_data('models/eateries.json')
orders = load_data('models/orders.json')
items = load_data('models/items.json')

# Save data back to JSON files (if needed, e.g., for updates)
def save_data(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

# GET request to retrieve user information
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    if request.method == "GET":
        user = users.get(str(user_id))  # Use string key for JSON compatibility
        if user:
            return jsonify(user)
        return jsonify({"status": "error", "feedback": "User not found"}), 404

# POST request to add user information, only checks if user exists
@app.route('/users', methods=['POST'])
def add_user():
    if request.method == "POST":
        try:
            # Get the data from the POST request
            new_user = request.json  

            # Ensure the request contains the "id" field
            user_id = str(new_user.get("id"))
            if not user_id:
                return jsonify({"status": "error", "feedback":"'id' is required"}), 400

            # Check if the user already exists in the database
            if user_id in users:
                return jsonify({"status":"success", "feedback": "User already exists"}), 400
            else:
                return jsonify({"status":"success", "feedback": "User does not exist"}), 201

        except KeyError as e:
            # Handle cases where the expected key is missing from JSON
            return jsonify({"status": "error","feedback": f"Missing key in request: {str(e)}"}), 400

        except Exception as e:
            # Catch-all for unexpected errors
            return jsonify({"status": "error","feedback": f"An error occurred: {str(e)}"}), 500
    
# POST request to create user information
@app.route('/createUser', methods=['POST'])
def create_user():
    if request.method == "POST":
        new_user = request.json  # Get the data from the POST request

        user_id = str(new_user.get("id")) # Assume "id" is part of the data
        password = new_user.get("password")

        if not user_id or not password:  # Check if both "id" and "password" are provided
            return jsonify({"status":"error","feedback": "Both 'id' and 'password' are required"}), 400

        if user_id in users:
            return jsonify({"status":"error","feedback": "User already exists"}), 400
        
        else:
            users[user_id] = new_user
            save_data(users, 'users.json')  # Save changes to the file
            return jsonify({"status":"success","feedback": "User added successfully"}), 201

# GET request to retrieve eatery information
@app.route('/eateries/<eatery_id>', methods=['GET'])
def get_eatery(eatery_id):
    if request.method == "GET":
        eatery = eateries.get(str(eatery_id))  # Use string key for JSON compatibility
        if eatery:
            return jsonify(eatery)
        return jsonify({"status":"error","feedback": "Eatery not found"}), 404

# POST request to add eatery information
@app.route('/eateries', methods=['POST'])
def add_eatery():
    if request.method == "POST":
        new_eatery = request.json  # Get the data from the POST request
        eatery_id = str(new_eatery.get("id"))  # Assume "id" is part of the data

        if not eatery_id:  # Check if "id" are provided
            return jsonify({"status":"error","feedback": "'id' are required"}), 400
        
        if eatery_id in eateries:
            return jsonify({"status":"error","feedback": "Eatery already exists"}), 400
        eateries[eatery_id] = new_eatery
        save_data(eateries, 'eateries.json')  # Save changes to the file
        return jsonify({"status":"success","feedback": "Eatery added successfully"}), 201
    
# GET request to retrieve order information
@app.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    if request.method == "GET":
        order = orders.get(str(order_id))  # Use string key for JSON compatibility
        if order:
            return jsonify(order)
        return jsonify({"status":"error","feedback": "Order not found"}), 404

#GET request to retrieve all order
@app.route('/orders', methods=['GET'])
def get_orders():
    if request.method == "GET":
        if orders:
            return orders
        return jsonify({"status":"error","feedback": "No orders found"}), 404

# POST request to add order information
@app.route('/orders', methods=['POST'])
def add_order(order_id):
    if request.method == "POST":
        new_order = request.json  # Get the data from the POST request
        order_id = str(new_order.get("id"))  # Assume "id" is part of the data
        
        if not order_id:  # Check if "id" are provided
            return jsonify({"status":"error","feedback":"'id' is required"}), 400
        
        if order_id in orders:
            return jsonify({"status":"error","feedback":"Order already exists"}), 400
        orders[order_id] = new_order
        save_data(orders, 'orders.json')  # Save changes to the file
        return jsonify({"status":"success","feedback":"Order added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)