# Project Title

A brief description of your project.

## Requirements

- Python 3.x
- Flask
- PeeWee

## Installation

1. Clone the repository
2. Create a virtual environment
3. Install dependencies with `pip install -r requirements.txt`

## Usage

1. Run the Flask app with `python app.py`
2. Use tools like `curl` or Postman to interact with the API

## API Endpoints

- `GET /items`: Get a list of items
- `POST /items`: Create a new item
- `DELETE /items/<item_id>`: Delete an item by ID

## Example Initial Data

```python
initial_cars = [
    {
        "make": "Toyota",
        "model": "Camry",
        "year": 2020,
        "color": "Blue",
        "image": "https://s3.amazonaws.com/di-enrollment-api/toyota/models/2020/camry/colors/blue_streak_metallic.jpg",
        "electric": False,
    },
]

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "New Item"}' http://localhost:5000/items
