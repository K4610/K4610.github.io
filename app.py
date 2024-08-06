from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/process_text', methods=['POST'])
def process_text():
    data = request.json
    user_input = data.get('userInput')
    
    # Process the input text (e.g., convert to uppercase)
    processed_text = user_input.upper()  # Replace with your actual processing logic

    return jsonify({"processedText": processed_text})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
