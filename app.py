from flask import Flask, jsonify, request, Response
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
    # args = request.args.get("name")
    resp = requests.get("https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/ka/json/?currencies=USD&date=2025-11-21")
    return Response(resp.text, mimetype='application/json')

@app.route("/<string:cur>")
def currency(cur):
    return cur