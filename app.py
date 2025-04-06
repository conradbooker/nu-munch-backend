# from flask import Flask, request, jsonify
    
# app = Flask(__name__)

# # Create route for eateries
# @app.route('/eateries', methods=['GET'])
# def eateries_route():
#     """Route to handle eateries."""
#     eateries = request.args.get('eateries')
#     if eateries:
#         return jsonify({"status": "success", "feedback": f"{eateries}"}), 200
#     else:
#         return jsonify({"status": "error", "feedback": "Missing eateries"}), 400

# # Create route for items in eateries
# @app.route('/eateries/<eatery_id>/items', methods=['GET'])
# def items_route(eatery_id):
#     items = request.args.get('items')
#     """Route to handle items in a specific eatery."""
#     if eatery_id:
#         return jsonify({"status": "success","feedback": f"{items}"}), 200
#     else:
#         return jsonify({"status": "error", "feedback": "Missing items"}), 400

# # Create route for user
# @app.route('/users/<user_id>', methods=['GET', 'POST'])
# def user_route(user_id):
#     """Route to handle user-related actions."""
#     if request.method == "GET":
#         if user_id:
#             return jsonify({"status": "success", "feedback": f"{user_id}"}), 200
#         else:
#             return jsonify({"status": "error", "feedback": "Missing user"}), 400
    
#     if request.method == "POST":       
#         data = request.get_json()

#         if not data:
#             return jsonify({"status": "error", "feedback": "Missing body data"}), 400
        
#         user_data = data.get('user_data')
        
#         if not user_data:
#             return jsonify({"status": "error", "feedback": "Missing user_data in the request body"}), 400
        
#         return jsonify({"status": "success", "feedback": f"{user_data}"}), 200

# # Create route for specific orders
# @app.route('/order/<order_id>', methods=['GET','POST'])
# def order_route(order_id):
#     """Route to handle orders for a specific eatery."""
#     if request.method == "GET":
#         if order_id:
#             return jsonify({"status": "success", "feedback": f"{order_id}"}), 200
#         else:
#             return jsonify({"status": "error", "feedback": "Missing order ID"}), 400
    
#     if request.method == "POST":
#         data = request.get_json()

#         if not data:
#             return jsonify({"status": "error", "feedback": "Missing body data"}), 400
        
#         order_data = data.get('order_data')
        
#         if not order_data:
#             return jsonify({"status": "error", "feedback": "Missing order_data in the request body"}), 400
        
#         return jsonify({"status": "success", "feedback": f"{order_data}"}), 200
        
# # Create route for all orders
# @app.route('/orders', methods=['GET'])
# def orders_route():
#     """Route to handle orders."""
#     orders = request.args.get('orders')
#     if orders:
#         return jsonify({"status": "success", "feedback": f"{orders}"}), 200
#     else:
#         return jsonify({"status": "error", "feedback": "Missing all orders"}), 400

# if __name__ == '__main__':
#     app.run(debug=True)