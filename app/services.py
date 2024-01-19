import requests
import uuid

from flask import jsonify

from app import app, db

def reserve_item(item_name):
    """Mock Function to reserve an item and generate reservation ID.
       Parameters:
        item_name(String): Name of the item to be reserved.
            """
    if item_name:
        # Generate a random reservation ID
        random_reservation_id = str(uuid.uuid4())
        reservation_id = {"reservation_id": random_reservation_id}
        return jsonify(reservation_id)
    else:
        # Handle the case when item_name is missing
        return jsonify({"error": "Invalid request. 'item' parameter is missing."}), 400


def perform_background_reservation(item, item_name):
    """Perform background reservation for an item using an external service.
       Parameters:
        item: Item model instance to be updated with reservation information.
        item_name(String): Name of the item to be reserved.
            """
    with app.app_context():
        # Call the /reserve endpoint with json body
        reserve_response = requests.post('http://127.0.0.1:5000/reserve', json={"name": item_name})

        if reserve_response.status_code == 200:
            reservation_id = reserve_response.json().get('reservation_id')

            item.reservation_id = reservation_id
            db.session.add(item)
            db.session.commit()
        else:
            # Handle the case when reservation fails
            print(f"Failed to reserve item {item_name}")



