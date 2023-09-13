from flask import Flask, request, jsonify, render_template
from levenshtein_distance import levenshtein_distance

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['GET'])
def calculate():
    string1 = request.args.get('string1')
    string2 = request.args.get('string2')
    
    distance = levenshtein_distance(string1, string2)
    
    return jsonify({'distance': distance})

if __name__ == '__main__':
    app.run(debug=True)
