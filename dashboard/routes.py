from flask import Flask, render_template, request
import pandas as pd
import json
import requests
import xml.etree.ElementTree as ElementTree
import re

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("landing.html")

@app.route("/dashboard", methods=['POST'])
def dashboard():
    query = request.form.get("query")
    print("got query of",query)
    #printed in the command window for tracking purposes


    key = "tElckxfXrsUO6Y6xHpBcA"
    #secret = "S47cOPu8AGUYha4LUUyUq0chuIbnrCkxgdnrwVanYg"
    url = "https://www.goodreads.com/book/title.xml?"
    params = {
        "key" : key,
        "title" : query
    }

    result = requests.get(url, params=params)
    res = ElementTree.fromstring(result.content)

    filtered = re.compile('<.*?>')
    book_description = re.sub(filtered, '', res[1][16].text)

    rating_distribution = str(res[1][17][13].text).split("|")
    rating_distribution = [i[2:] for i in rating_distribution]
    rating_distribution.pop()

    book_title = str(res[1][1].text)
    book_author = str(res[1][26][0][1].text)
    reviews_count = str(res[1][17][3].text)
    average_rating = str(res[1][18].text)
    num_pages = str(res[1][19].text)
    #data = {"book_ISBN" : str(res[1][2].text)}

    positive_counts = int(rating_distribution[0]) + int(rating_distribution[1]) + int(int(rating_distribution[0])/2)
    negative_counts = int(rating_distribution[3]) + int(rating_distribution[4]) + int(int(rating_distribution[0])/2)

    return render_template("dashboard.html", query=query, book_description = book_description,
    reviews_count=reviews_count, rating_distribution = rating_distribution, book_title = book_title, 
    book_author = book_author, average_rating = average_rating, num_pages = num_pages,
    positive_counts=positive_counts, negative_counts = negative_counts)