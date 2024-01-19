import threading

from flask import request, jsonify

from app.services import perform_background_reservation
from app import app, db
from app.models import Item


@app.route('/items', methods=['POST'])
def add_item():
    """Post API call to add an item to the cart.
            """
    response = request.get_json()
    name = response.get('name')
    quantity = response.get('quantity', 1)

    # save item in the database
    item = Item(name=name, quantity=quantity, reservation_id=None)
    db.session.add(item)
    db.session.commit()

    # Run the external reservation service in the background
    threading.Thread(target=perform_background_reservation, args=(item, name), daemon=True).start()

    return jsonify({'message': 'Item added to the cart successfully'})


@app.route('/reserve', methods=['POST'])
def reserve_item_route():
    """Mock API call to reserve an item added to the cart.
            """
    from app.services import reserve_item
    response = request.get_json()
    name = response.get('name')
    return reserve_item(name)


# API to fetch items from the cart
@app.route('/items', methods=['GET'])
def get_items():
    """Get API call to fetch items added to the cart.
            """
    with app.app_context():
        items = Item.query.all()
        return jsonify(
            [{'name': item.name, 'quantity': item.quantity, 'reservation_id': item.reservation_id} for item in items])
