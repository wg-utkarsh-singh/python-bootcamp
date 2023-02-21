from flask import Flask, request, jsonify

app = Flask(__name__)

countries = [
    {"id": 1, "name": "India", "capital": "New Delhi", "area": 3_287_263},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7_617_930},
]


def _find_next_id():
    return max(country["id"] for country in countries) + 1


@app.get("/countries")
def get_countries():
    return jsonify(countries)


@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415
