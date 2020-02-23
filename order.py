from flask import Flask
import requests , json

app = Flask(__name__)

@app.route('/')
def root():
    response = requests.get("http://192.168.56.101:5000/query_item/2")
    
    return response.json()

@app.route('/buy/<_id>')
def buy(_id):
    response = requests.get("http://192.168.56.101:5000/query_item/"+_id)
    obj = response.json()
    ammount = obj["books"][0]["ammount"]
    
    if (ammount>0):
       response2 = requests.get("http://192.168.56.101:5000/update_dec_ammount/"+_id)
       obj2 = response2.json()
       ammount2 = obj2["books"][0]["ammount"]
       if (response2.json()!= None):
          return str(ammount2) 
          
    return str(ammount) 
