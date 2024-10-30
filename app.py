from flask import Flask, render_template, jsonify
from api_client import get_useless_fact

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_fact', methods=['GET'])
def get_fact():
    fact_text = get_useless_fact()
    return jsonify({'fact': fact_text})

if __name__ == '__main__':
    app.run(debug=True)
