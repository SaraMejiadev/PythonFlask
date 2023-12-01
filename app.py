# app.py
from flask import Flask, jsonify, request
from peewee import SqliteDatabase, Model, CharField, IntegerField, BooleanField

# Initialize Flask app
app = Flask(__name__)

# Set up SQLite database
db = SqliteDatabase('cars.db')

# Define the Car model
class Car(Model):
    make = CharField()
    model = CharField()
    year = IntegerField()
    color = CharField()
    image = CharField()
    electric = BooleanField()

    class Meta:
        database = db

# Create tables if not exist
db.connect()
db.create_tables([Car], safe=True)

# Initial data for demonstration
initial_cars = [
    {
        "make": "Toyota",
        "model": "Camry",
        "year": 2020,
        "color": "Blue",
        "image": "https://s3.amazonaws.com/di-enrollment-api/toyota/models/2020/camry/colors/blue_streak_metallic.jpg",
        "electric": False,
    },
    {
        "make": "Tesla",
        "model": "Model S",
        "year": 2022,
        "color": "Red",
        "image": "https://hips.hearstapps.com/hmg-prod/images/2022-tesla-model-s-plaid-mmp-1-1628541250.png?crop=0.798xw:0.892xh;0.0481xw,0&resize=1200:*",
        "electric": True,
    },
        {
        "make": "Honda",
        "model": "Pilot",
        "year": 2023,
        "color": "Silver",
        "image": "https://di-uploads-pod3.dealerinspire.com/germainhondaofannarbor/uploads/2023/03/2303-Honda-Pilot-EX-L-Lunar-Silver-Metallic.jpg",
        "electric": False,
    },
        {
        "make": "Ford",
        "model": "Bronco",
        "year": 2024,
        "color": "Green",
        "image": "https://images.dealer.com/ddc/vehicles/2024/Ford/Bronco/SUV/color/Eruption%20Green%20Metallic-FA-38,76,68-640-en_US.jpg",
        "electric": False,
    },
    
]

# Populate initial data
with db.atomic():
    Car.insert_many(initial_cars).execute()

# Routes
@app.route('/cars', methods=['GET'])
def get_cars():
    cars = [{'id': car.id, 'make': car.make, 'model': car.model, 'year': car.year,
             'color': car.color, 'image': car.image, 'electric': car.electric}
            for car in Car.select()]
    return jsonify({'cars': cars})

if __name__ == '__main__':
    app.run(debug=True)
