# Inventory Manager API

A simple inventory management API built with FastAPI.

## Installation

```bash
pip install -r requirements.txt
```

## Run the API

```bash
uvicorn project:app --reload
```

The API will be available at `http://127.0.0.1:8000`

## API Endpoints

- `GET /` - Root endpoint
- `GET /items` - Get all items
- `GET /items/{item_id}` - Get a specific item
- `POST /items` - Create a new item
- `PUT /items/{item_id}` - Update an item
- `DELETE /items/{item_id}` - Delete an item

## Interactive API Docs

Visit `http://127.0.0.1:8000/docs` for interactive API documentation.
