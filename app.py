from flask import Flask

import controllers
app = Flask(__name__, static_url_path='', static_folder='static')

GET = 'GET'
PUT = 'PUT'
POST = 'POST'
DELETE = 'DELETE'

app.add_url_rule('/users/<string:user_id>', view_func=controllers.users, methods = [GET,POST,PUT])
app.add_url_rule('/useremail/<string:email>', view_func=controllers.get_user_by_email, methods = [GET])
app.add_url_rule('/orders/<string:order_id>', view_func=controllers.orders, methods = [GET,POST,PUT])
app.add_url_rule('/orders', view_func=controllers.all_orders, methods = [GET,POST])
app.add_url_rule('/order_length', view_func=controllers.orders_length, methods = [GET])
app.add_url_rule('/eateries', view_func=controllers.all_eateries, methods = [GET])
app.add_url_rule('/eateries/<string:eatery_id>', view_func=controllers.eateries, methods = [GET])
app.add_url_rule('/eateries/<string:eatery_id>/items', view_func=controllers.eateries_items, methods = [GET])
app.add_url_rule('/items/<string:item_id>', view_func=controllers.items, methods = [GET])

if __name__ == '__main__':
    app.run(debug=True)