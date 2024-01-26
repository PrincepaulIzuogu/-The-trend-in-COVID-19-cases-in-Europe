from flask import Flask, request, jsonify, send_file, redirect, url_for
import json
from uuid import uuid4

app = Flask(__name__)

# Global variable to store FHIR bundle data
fhir_bundle_data = []

@app.route('/receive_fhir_bundle', methods=['POST'])
def receive_fhir_bundle():
    try:
        # Assuming the incoming data is a list of Immunization resources
        data = request.get_json()

        # Process and validate the data if needed

        # Append the data to the global variable
        fhir_bundle_data.extend(data)

        # Store the data in a file
        with open('fhir_bundle_data.json', 'w') as file:
            json.dump(fhir_bundle_data, file, indent=2)

        return jsonify({'status': 'success'})

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/get_fhir_bundle', methods=['GET'])
def get_fhir_bundle():
    try:
        # Return the stored FHIR bundle data
        return jsonify(fhir_bundle_data)

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

# Route for serving index.html
@app.route('/')
def index():
    return send_file('templates/index.html')

# Route for serving script.js
@app.route('/script.js')
def get_script():
    return send_file('static/script.js')

# Route for serving dough.js
@app.route('/dough.js')
def get_dough_script():
    return send_file('static/dough.js')

# Route for serving styles.css
@app.route('/styles.css')
def get_styles():
    return send_file('static/styles.css')

# Route for serving data.json
@app.route('/extra_fields.json')
def get_data():
    return send_file('static/extra_fields.json')

# Route for serving data.json
@app.route('/data.json')
def get_data():
    return send_file('static/data.json')


# Route for serving flags from the root directory
@app.route('/flags/<filename>')
def get_flag(filename):
    return send_file(f'flags/{filename}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


