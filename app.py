from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process_text', methods=['POST'])
def process_text():
    data = request.json
    user_input = data.get('userInput')
    
    # Process the input text (for example, convert to uppercase)
    processed_text = user_input.upper()  # Replace this with your actual processing logic

    return jsonify({"processedText": processed_text})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
