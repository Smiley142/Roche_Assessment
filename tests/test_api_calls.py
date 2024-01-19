import unittest

from flask import json

from app import app, db


class ShoppingCartAPITestCase(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.app = app.test_client()

        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_item_to_cart(self):
        """function to test adding items to the cart"""
        response = self.app.post("/items", json={"name": "Product1", "quantity": 2})
        # Check the response status code
        self.assertEqual(response.status_code, 200)

    def test_get_items_in_cart(self):
        """function to test fetching items added to the cart"""
        self.app.post("/items", json={"name": "Product1", "quantity": 2})
        response = self.app.get("/items")
        data = json.loads(response.get_data(as_text=True))
        # Check the response status code
        self.assertEqual(response.status_code, 200)
        # Check the response JSON data
        self.assertEqual(data[0]["name"], "Product1")
        self.assertEqual(data[0]["quantity"], 2)

    def test_reserve_item(self):
        """function to test reserving items added to the cart"""
        # Make a request to the /reserve endpoint
        response = self.app.post("/reserve", json={"name": "test_item"})

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check the response JSON data
        data = response.get_json()
        self.assertIn("reservation_id", data)


if __name__ == "__main__":
    unittest.main()
