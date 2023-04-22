from flask import Flask, request, jsonify, render_template
from algorithm_layer import process_image
from database_layer import store_data, query_data
import json

app = Flask(__name__)

# Render the HTML template for user input
@app.route('/')
def index():
    return render_template('selection.html')

#Queries the database and returns the JSON data
@app.route('/data', methods=['GET'])
def data():
    data = query_data()
    return jsonify(data)

# Handle image uploads and user information
@app.route('/upload', methods=['POST'])
def upload():
    # Get user information from the request
    user_info = {
        'phone': request.form.get('phone'),
        'address': request.form.get('address'),
        'passport': request.form.get('passport')
    }

    # Get the uploaded image
    image = request.files.get('image')

    # Call the algorithm layer to process the image
    result = process_image(image)

    if result['status'] == 'success':
        # Store the data in the database
        store_data(user_info, image, result['text'])

        # Return the result to the user
        return jsonify(result)
    else:
        # Return the error message to the user
        return jsonify(result), 400

# Runs the Flask app in debug mode
if __name__ == '__main__':
    app.run(debug=True)

