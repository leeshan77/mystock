from flask import Flask, request, render_template, redirect, jsonify

import requests
from bs4 import BeautifulSoup

# import pymongo
# from pymongo import MongoClient
# from pymongo.cursor import CursorType

app = Flask(__name__)

# my_client = MongoClient("mongodb://localhost:27017/")
# host = "localhost"
# port = 27017
# my_client = MongoClient(host, port)

# username = 'davelee'
# password = 'korea123'
# my_client = pymongo.MongoClient('mongodb://%s:%s@www.funcoding.xyz' % (username, password))

# mydb = my_client['stock04']
# mycol = mydb['sise']

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sise')
def stock_bs4():

    company_codes = ["005930", "000660", "005380"]

    prices = []
    for item in company_codes:
        now_price = get_price(item)
        prices.append(now_price)

    # mydb.sise.insert_one({'name': '삼성', 'sise': prices[0]})
    # mydb.sise.insert_one({'name': 'sk', 'sise': prices[1]})
    # mydb.sise.insert_one({'name': '현대', 'sise': prices[2]})

    # list = mycol.find({}, {"_id":0, "name":1, "sise":1})

    # mysise = []
    # for x in list:
    #     mysise.append(x)

    return jsonify({'result':'success', 'stocklist':'my test list'})


def get_bsoup(company_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code

    result = requests.get(url)
    if result.status_code == 200:
        bs_obj = BeautifulSoup(result.content, "html.parser")
        return bs_obj
    else:
        print(result.status_code)

def get_price(company_code):
    bs_obj = get_bsoup(company_code)
    no_today = bs_obj.find("p", {"class": "no_today"})
    blind = no_today.find("span", {"class": "blind"})

    now_price = blind.text
    return now_price

if __name__ == '__main__':
    app.run(debug=True)




