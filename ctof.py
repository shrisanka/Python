from flask import Flask, request, jsonify

app = Flask(__name__)

def pounds_to_kg(pounds):
    kilograms = pounds * 0.453592
    return kilograms

def feet_to_cm(feet):
    centimeters = feet * 30.48
    return centimeters

@app.route('/convert/pounds_to_kg', methods=['POST'])
def convert_pounds_to_kg():
    try:
        data = request.get_json()
        if 'pounds' not in data or not isinstance(data['pounds'], (int, float)):
            raise ValueError("Invalid input. Please provide 'pounds' as a number.")
        
        pounds = data['pounds']
        kilograms = pounds_to_kg(pounds)
        return jsonify({'kilograms': kilograms}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An internal server error occurred.'}), 500

@app.route('/convert/feet_to_cm', methods=['POST'])
def convert_feet_to_cm():
    try:
        data = request.get_json()
        if 'feet' not in data or not isinstance(data['feet'], (int, float)):
            raise ValueError("Invalid input. Please provide 'feet' as a number.")
        
        feet = data['feet']
        centimeters = feet_to_cm(feet)
        return jsonify({'centimeters': centimeters}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An internal server error occurred.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
