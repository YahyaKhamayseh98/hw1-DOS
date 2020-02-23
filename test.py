from flask import Flask 
import requests, json
app = Flask(__name__)

@app.route('/')
def route():
    print("")
    print("Welcome to Bazar.come") 
    while 1>0:
       print("")
       print("Store services:")
       print("1. Buy ")
       print("2. Lookup ")
       print("3. Search ")
       print("")
       index = input("Please enter the index of the service to proceed it:")
       if int(index) == 1:
          print("")
          _id = input("please enter the number of the book you want to buy:")
          response = requests.get("http://192.168.56.103:5000/buy/"+_id)
          print("")
          print(response.json())
          print("")
       if int(index) == 2:
          print("")
          _id = input("please enter the number of the book you want to lookup on:")
          response = requests.get("http://192.168.56.103:5000/lookup/"+_id)
          print("")
          print(response.json())
          print("")
       if int(index) == 3:
          print("")
          _topic = input("please enter the topic of the books you want to search for:")
          response = requests.get("http://192.168.56.103:5000/search/"+_topic)
          print("")
          print(response.json())
     
    return 'Bazar.com'
    
    
