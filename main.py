from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get_location', methods=['GET'])
def get_location():
    latitude = 48.148596
    longitude = 17.107754

    try:
        latitude = float(latitude)
        longitude = float(longitude)

        if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
            return jsonify({
                'status': 'error',
                'message': 'Недопустимые значения координат. Широта: -90..90, Долгота: -180..180'
            }), 400

        wgs84_coords = f"loc:{latitude}@{longitude}"
        return jsonify({
            'status': 'success',
            'coordinates': wgs84_coords
        }), 200

    except (TypeError, ValueError):
        return jsonify({
            'status': 'error',
            'message': 'Координаты должны быть числами'
        }), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    # lsof -i :{port}
    # kill -9 {number_of_task}
    # to kill task which using this port
