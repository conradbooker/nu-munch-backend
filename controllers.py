from flask import Flask, request, jsonify
import json
import sys, os
import time

rootPath = os.path.abspath(os.path.join(os.path.dirname(__file__), 'models', ''))
sys.path.append(rootPath)

def load_data(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

usersData = load_data('models/users.json')
eateriesData = load_data('models/eateries.json')
ordersData = load_data('models/orders.json')
itemsData = load_data('models/items.json')

def getData(path):
    # print(f"oop path is {path}")
    readFile = open(path)
    jsonData = json.load(readFile)
    readFile.close()
    return jsonData

def save_data(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

def users(user_id):
    if request.method == "GET":
        user = usersData.get(str(user_id))  # Use string key for JSON compatibility
        if user:
            return jsonify(user)
        return jsonify({"status": "error", "feedback": "User not found"}), 404
    
    if request.method == "POST":
        try:
            new_user = request.json  

            user_id = str(new_user.get("id"))
            if not user_id:
                return jsonify({"status": "error", "feedback":"'id' is required"}), 400

            # Check if the user already exists in the database
            if user_id in usersData:
                return jsonify({"status":"success", "feedback": "User already exists"}), 400
            else:
                return jsonify({"status":"success", "feedback": "User does not exist"}), 201

        except KeyError as e:
            # Handle cases where the expected key is missing from JSON
            return jsonify({"status": "error","feedback": f"Missing key in request: {str(e)}"}), 400

        except Exception as e:
            # Catch-all for unexpected errors
            return jsonify({"status": "error","feedback": f"An error occurred: {str(e)}"}), 500
    elif request.method == "GET":
        user = usersData.get(str(user_id))  # Use string key for JSON compatibility
        if user:
            return jsonify(user)
        return jsonify({"status": "error", "feedback": "User not found"}), 404

def order(order_id):
    if request.method == "GET":
        order = ordersData.get(str(order_id))  # Use string key for JSON compatibility
        if order:
            return jsonify(order)
        return jsonify({"status":"error","feedback": "Order not found"}), 404

    
    if request.method == "POST":
        new_user = request.json  # Get the data from the POST request

        user_id = str(new_user.get("id")) # Assume "id" is part of the data
        password = new_user.get("password")

        if not user_id or not password:  # Check if both "id" and "password" are provided
            return jsonify({"status":"error","feedback": "Both 'id' and 'password' are required"}), 400

        if user_id in usersData:
            return jsonify({"status":"error","feedback": "User already exists"}), 400
        
        else:
            usersData[user_id] = new_user
            save_data(usersData, 'users.json')  # Save changes to the file
            return jsonify({"status":"success","feedback": "User added successfully"}), 201
    elif request.method == "GET":
        orders = load_data('orders.json')
        order = orders.get(str(order_id))  # Use string key for JSON compatibility
        if order:
            return jsonify(order)
        return jsonify({"status":"error","feedback": "Order not found"}), 404

def orders():
    if request.method == "GET":
        if ordersData:
            return ordersData
        return jsonify({"status":"error","feedback": "No orders found"}), 404

def eateries(eatery_id):
    if request.method == "GET":
        eatery = eateriesData.get(str(eatery_id))  # Use string key for JSON compatibility
        if eatery:
            return jsonify(eatery)
        return jsonify({"status":"error","feedback": "Eatery not found"}), 404

def eateries_items(eatery_id):
    eateries_data = {}  # Replace with actual data loading logic
    eateries_data = [key for key, value in itemsData.items() if str(value.get("eatery_id")) == str(eatery_id)]
    return jsonify(eateries_data) if eateries_data else jsonify({"status": "error", "feedback": "No items found"}), 404

def items(item_id):
    if request.method == "GET":
        item = itemsData.get(str(item_id))  # Use string key for JSON compatibility
        if item:
            return jsonify(item)
        return jsonify({"status":"error","feedback": "Item not found"}), 404