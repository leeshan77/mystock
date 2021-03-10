from flask import Flask, request, render_template, jsonify

import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ajax', methods=['POST'])
def ajax():
    data = request.get_json()
    print(data)

    return jsonify(result = "success", result2= data)

if __name__ == '__main__':
    app.run(debug=True)




