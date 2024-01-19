# Shopping Cart API

## How to Use

1. Open the project in PyCharm or any IDE.
2. Configure Python interpreter and select latest version of Python.
3. Install dependencies: `pip install -r requirements.txt`
4. Run the application: `python main.py`

## How to test the application

1. Test the endpoints in the postman or any API testing application.
2. Configure the API base URL (e.g., `http://localhost:5000/`).
3. Example Post Request
   - **Add Item to Cart:**
     - Endpoint: `POST /items`
     - Header: Content-Type- application/json
     - Body (JSON):
       ```json
       {
         "name": "Product1",
         "quantity": 2
       }
       ```

### Endpoints

- `GET /items`: List all items in the cart
- `POST /items`: Add a new item to the cart (provide name and optional quantity)
- `POST /reserve`: Reserve an item using an external service (provide item name in the JSON body)


## Self-assessment

### What is missing and couldn’t be done anymore?

- Detailed error handling and logging for production use.
- Unit tests for the background reservation process.
- Authentication and authorization mechanisms for API security.

### Which elements should be improved to make it production-ready?

- Implement a production-ready database (SQLite is used for simplicity in this example).
- Implement a task queue (e.g., Celery) for background jobs.
- Implement a proper error handling and logging strategy.
- Add security measures like input validation and authentication.
- Add dynamic features to make it more user friendly in real-time
- Cover different scenarios in unit tests to be production ready. 

### Were there any topics you were struggling with?

- N/A (since code readability, structure, and simplicity were prioritized).


## Tooling and Library Choices
### Web Framework: Flask

- *Why Flask?*
  - Flask is a minimalistic, lightweight framework and allows for quick development that fits our project's needs without unnecessary complexity.

### Database Toolkit: SQLAlchemy

- *Why SQLAlchemy?*
  - SQLAlchemy provides a powerful Object-Relational Mapping (ORM) system, simplifying database interactions.

### Development Database: SQLite

- *Why SQLite?*
  - SQLite is a file-based database, simplifying development without the need for a separate server and it requires minimal setup, making it ideal for local development and testing.

### Background Jobs: Threading

- *Why Threading?*
  - Threading is a straightforward solution for handling background jobs without the complexity of more extensive frameworks.

I have used this framework/library as I have experience working with them and they are perfect for this project needs (quick and simple).