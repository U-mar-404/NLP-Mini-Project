from flask import Flask, request, jsonify
from flask_cors import CORS
import models

app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    query      = data.get('query', '')
    use_cosine = data.get('cosine', True)
    use_bayes  = data.get('bayes', False)

    response = {'query': query}

    if use_cosine:
        response['similar_cases'] = models.find_similar_cases(query)

    if use_bayes:
        outcome, confidence = models.predict_outcome(query)
        response['predicted_outcome'] = outcome
        response['confidence'] = confidence

    return jsonify(response)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'running'})

if __name__ == '__main__':
    print("🚀 Starting Legal Case Finder API...")
    app.run(debug=True, port=5000)