from flask import Flask, render_template, request
from api_integration.flight_prices import get_flight_price


app = Flask(__name__)

@app.route('/test')
def index():
    return render_template('index.html')

@app.route('/')
def search_prices():
    # Getting Form Data
    source_airport_code = request.form['source_airport_code']
    destination_airport_code = request.form['destination_airport_code']
    departure_date = request.form['departure_date']
    return_date = request.form.get('return_date')
    number_people = request.form['number_people']

    # Call get_flight_price function
    flights_data = get_flight_price(
        source_airport_code,
        destination_airport_code,
        departure_date,
        number_people,
        return_date
    )

    return render_template('search_flight.html', flights_data=flights_data)