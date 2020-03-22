import json
from flask import Flask, request, Response

from models import User, Item, Bid
app = Flask(__name__)

items = Item()
for i in range(6):
    items.add({'title': 'item %d' % i})


users = User()
users.add({'name': 'Taweel'})
bids = Bid()


@app.route('/api/v1/items/<int:item_id>/bid/', methods=['POST'])
def record_bid(item_id):
    # check if id exists
    item = items.get(item_id)
    if not item:
        abort(404)
    user_id = request.json.get('user_id', 0)
    amount = request.json.get('amount', 0)
    bids.add({'item_id': item_id, 'user_id': user_id, 'amount': amount})
    return Response(status=201)


@app.route('/api/v1/items/<int:item_id>/bids/', methods=['GET'])
def get_all_item_bids(item_id):
    # check if id exists
    item = items.get(item_id)
    if not item:
        abort(404)
    return Response(json.dumps(bids.get_all_for_item(item_id)), status=200, content_type='application/json')


@app.route('/api/v1/items/<int:item_id>/bids/winnings/', methods=['GET'])
def get_winning_bid_for_items(item_id):
    # check if id exists
    item = items.get(item_id)
    if not item:
        abort(404)
    return Response(json.dumps(bids.get_winning_bid(item_id)), status=200, content_type='application/json')


@app.route('/api/v1/user/<int:user_id>/items/', methods=['GET'])
def get_all_items_for_user(user_id):
    user = users.get(id=user_id)
    if not user:
        abort(404)
    return Response(json.dumps(bids.get_all_for_user(user_id)), status=200, content_type='application/json')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8989)
