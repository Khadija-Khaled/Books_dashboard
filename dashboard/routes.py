from flask import Flask, render_template, request
import pandas as pd
import json
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("landing.html")

@app.route("/dashboard", methods=['POST'])
def dashboard():
    query = request.form.get("query")
    print("got query of",query)


    key = "tElckxfXrsUO6Y6xHpBcA"
    secret = "S47cOPu8AGUYha4LUUyUq0chuIbnrCkxgdnrwVanYg"
    url = "https://www.goodreads.com/book/review_counts.json?"
    params = {
        "isbns" : query,
        "key" : key
    }

    res = requests.get(url, params=params)
    res = json.loads(res.text)
    print(res)
    data = { 
            "book_id": str(res['books'][0]['id']), 
            "ratings_count": str(res['books'][0]['ratings_count']),
            # "temp": str(res['main']['temp']) + ' C', 
            # "pressure": str(res['main']['pressure']) + " hPa", 
            # "humidity": str(res['main']['humidity']) + "%",
            # "wind": str(res['wind']['speed']) + ' m/s'
    } 
    print(data)
