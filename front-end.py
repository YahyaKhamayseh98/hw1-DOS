from flask import Flask, jsonify 
import requests, json 
app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'
    
@app.route('/buy/<_id>')
def buy(_id):
    response = requests.get("http://192.168.56.102:5000/buy/"+_id)
    if (response.json()>0):
        return jsonify("Purchase is done !")
    return jsonify("The Ordered book is not existed in the stock any more !")
    
@app.route('/lookup/<_id>')
def lookup(_id):
    response = requests.get("http://192.168.56.101:5000/query_item/"+_id)
    return response.json()
    
@app.route('/search/<_topic>')
def search(_topic):
    response = requests.get("http://192.168.56.101:5000/query_sub/"+_topic)
    return response.json()
