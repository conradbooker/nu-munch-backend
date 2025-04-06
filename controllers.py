from flask import Flask, request, jsonify
import json
import sys, os
import time

rootPath = os.path.abspath(os.path.join(os.path.dirname(__file__), 'models', ''))
sys.path.append(rootPath)


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
    file_path = os.path.join(rootPath, 'users.json')
    if request.method == 'GET':
        try:
            user_data = getData(file_path)[user_id]
            return jsonify({'status': 'success', 'feedback': user_data})
        except:
            return jsonify({'status': 'error', 'feedback': 'User not found'}), 404
    elif request.method == 'POST':
        new_user = request.json
        save_data(new_user, file_path)
        return jsonify({'status': 'success', 'feedback': new_user}), 201
    elif request.method == "PUT":
        all_users = getData(file_path)
        if user_id in all_users:
            all_users[user_id] = request.json
            save_data(all_users, file_path)
            return jsonify({'status': 'success', 'feedback': all_users}), 201
        else:
            return jsonify({'status': 'error', 'feedback': 'Order not found'}), 404

def get_user_by_email(email):
    file_path = os.path.join(rootPath, 'users.json')
    all_users = getData(file_path)
    for user in all_users.values():
        if user['email'] == email:
            return jsonify({'status': 'success', 'feedback': user})
    return jsonify({'status': 'error', 'feedback': 'User not found'}), 404


def orders(order_id):
    file_path = os.path.join(rootPath, 'orders.json')
    if request.method == 'GET':
        orders_data = getData(file_path)
        for order in orders_data:
            if order['id'] == order_id:
                return jsonify({'status': 'success', 'feedback': order})
        return jsonify({'status': 'error', 'feedback': 'Order not found'}), 404
    elif request.method == 'POST':
        new_order = request.json
        new_order_id = request.json["id"]
        all_orders = getData(file_path)
        all_orders[new_order_id] = new_order
        save_data(all_orders, file_path)
        return jsonify({'status': 'success', 'feedback': all_orders}), 201
    elif request.method == 'PUT':
        all_orders = getData(file_path)
        if order_id in all_orders:
            all_orders[order_id] = request.json
            print(all_orders[order_id],all_orders[order_id],all_orders[order_id])
            save_data(all_orders, file_path)
            return jsonify({'status': 'success', 'feedback': all_orders}), 201
        else:
            return jsonify({'status': 'error', 'feedback': 'Order not found'}), 404


def all_orders():
    file_path = os.path.join(rootPath, 'orders.json')
    orders_data = getData(file_path)
    return jsonify({'status': 'success', 'feedback': orders_data})

def eateries(eatery_id):
    file_path = os.path.join(rootPath, 'eateries.json')
    eateries_data = getData(file_path)
    if eatery_id in eateries_data:
        return jsonify({'status': 'success', 'feedback': eateries_data[eatery_id]})
    else:
        return jsonify({'status': 'error', 'feedback': 'Eatery not found'}), 404
    
def all_eateries():
    file_path = os.path.join(rootPath, 'eateries.json')
    eateries_data = getData(file_path)
    return jsonify({'status': 'success', 'feedback': list(eateries_data.values())})


def eateries_items(eatery_id):
    file_path = os.path.join(rootPath, 'items.json')
    items_data = getData(file_path)
    eatery_items = [item for item in items_data.values() if item['eatery_id'] == eatery_id]
    return jsonify({'status': 'success', 'feedback': eatery_items})

def items(item_id):
    file_path = os.path.join(rootPath, 'items.json')
    items_data = getData(file_path)
    if item_id in items_data:
        return jsonify({'status': 'success', 'feedback': items_data[item_id]})
    else:
        return jsonify({'status': 'error', 'feedback': 'Item not found'}), 404



def orders_length():
    file_path = os.path.join(rootPath, 'orders.json')
    orders_data = getData(file_path)
    orders_data = {key: value for key, value in orders_data.items() if value.get('status') != 'In Progress'}
    return jsonify({'status': 'success', 'feedback': len(orders_data)})

"""
models/eateries.json:
    "0": {
        "id": "0",
        "name": "MOD Pizza",
        "description": "Pizza",
        "location": "42.05335, -87.67259",
        "area": "Norris"
    },
    "1": {
        "id": "1",
        "name": "847 Burger",
        "description": "Burger restaurant",
        "location": "42.05335, -87.67259",
        "area": "Norris"
    },
    ...

models/items.json:
    "0": {
        "id": "0",
        "name": "Pizza",
        "description": "Includes ... Please specify toppings below, and please specify if you want a water/etc in the description.",
        "options": [
            "Mozzarella", "Asiago", "Gorgonzola", "Parmesan",
            "Pepperoni", "Italian sausage", "Grilled chicken", "Spicy chicken sausage", "Ground beef", "Genoa salami",
            "Mushrooms", "Roasted red peppers", "Artichokes", "Black olives", "Jalapeños", "Red onions", "Diced tomatoes",
            "Basil", "Garlic", "Chickpeas",
            "Buffalo sauce", "BBQ sauce", "Garlic pesto", "Balsamic glaze"
        ],
        "eatery_id": "0" -> this eatery id matches the eatery id in the json
    },
    "1": {
        "id": "1",
        "name": "Salads",
        "description": "Includes ... Please specify toppings below, and please specify if you want a water/etc in the description.",
        "options": [
            "Romaine", "Mixed Spring Greens", "Vine-ripened Tomatoes", "Diced Cucumbers",
            "Sherry Dijon Vinaigrette", "Feta", "Sliced Red Onions", "Black Olives",
            "Mama Lil's Sweet Hot Peppas", "Chickpeas", "Greek Vinaigrette", "Asiago",
            "Aged Parmesan", "Croutons", "Caesar Dressing", "Arugula", "Mozzarella",
            "Genoa Salami", "Green Bell Peppers", "Zesty Tomato Vinaigrette"
        ],
        "eatery_id": "0"
    },

models/orders.json:
    {
        "id": "1",
        "status": "In Progress",
        "foodItem": {
        "id": "0",
        "name": "Pizza",
        "description": "Includes ... Please specify toppings below, and please specify if you want a water/etc in the description.",
        "options": [
            "Mozzarella"
        ],
        "eatery_id": "0" -> this eatery id matches the eatery id in the json
        },
        "locationStart": "",
        "locationEnd": "",
        "price": 19.99,
        "deliverer": "1001",
        "orderer": "2001"
    }

models/user.json:
{
    "id": "1",
    "name": "John Doe",
    "email": "john.doe@example.com",
    "currentDelivery": "101",
    "currentOrder": "202",
    "pastDeliveries": ["301", "302", "303"]
}
"""