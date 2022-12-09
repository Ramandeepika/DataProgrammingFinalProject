import requests
import time

from pymongo import MongoClient
from flask import Flask,render_template,jsonify,request


app = Flask(__name__)


client = MongoClient("mongodb://viral:Dextron123@ac-kftouh0-shard-00-00.c86othm.mongodb.net:27017,ac-kftouh0-shard-00-01.c86othm.mongodb.net:27017,ac-kftouh0-shard-00-02.c86othm.mongodb.net:27017/?ssl=true&replicaSet=atlas-13h81a-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.get_database('DataProgProject')




r1=requests.get("https://api.openweathermap.org/data/2.5/weather?q=paris&APPID=5e4b0773b43c02febad11a18afcde3ab")
r2=requests.get("https://api.openweathermap.org/data/2.5/weather?q=Mumbai&APPID=5e4b0773b43c02febad11a18afcde3ab")
r3=requests.get("https://api.openweathermap.org/data/2.5/weather?q=California&APPID=5e4b0773b43c02febad11a18afcde3ab")
r4=requests.get("https://api.openweathermap.org/data/2.5/weather?q=Toronto&APPID=5e4b0773b43c02febad11a18afcde3ab")

if r1.status_code == 200:
   Paris = r1.json()
   print(Paris)
   db.Paris.insert_one(Paris)
else:
   exit()
   
if r2.status_code == 200:
   Mumbai = r2.json()
   print(Mumbai)
   db.Mumbai.insert_one(Mumbai)
else:
   exit()  
      
if r3.status_code == 200:
   California = r3.json()
   print(California)
   db.California.insert_one(California)
else:
   exit() 
   
   
if r4.status_code == 200:
   Toronto = r4.json()
   print(Toronto)
   db.Toronto.insert_one(Toronto)
else:
   exit()        
        
        
@app.route('/')
def home():
    Paris = r1.json() # mexico
    Mumbai = r2.json() #pasto
    California = r3.json() #manchaes
    Toronto = r4.json() #sapro
    return render_template('home.html', **locals())     



# %% Paris
@app.route('/Paris')
def Paris():
    Paris = r1.json()
    cityName = Paris['name']
    country= Paris['sys']['country']
    localtime = Paris['timezone']    
    cityLongitud = Paris['coord']['lon']
    cityLatitud = Paris['coord']['lat']
    temp_K  = Paris['main']['temp'] -273
    humidity = Paris['main']['humidity']
    pressure = 0.0295*Paris['main']['pressure']    
    wind_speed = Paris['wind']['speed']

    return render_template('Paris.html', **locals())   


# %% Mumbai
@app.route('/Mumbai')
def Mumbai():
    Mumbai = r2.json()
    cityName = Mumbai['name']
    country= Mumbai['sys']['country']
    localtime = Mumbai['timezone']    
    cityLongitud = Mumbai['coord']['lon']
    cityLatitud = Mumbai['coord']['lat']
    temp_K      = Mumbai['main']['temp'] -273
    humidity = Mumbai['main']['humidity']
    pressure = 0.0295*Mumbai['main']['pressure']    
    wind_speed = Mumbai['wind']['speed']

    return render_template('Mumbai.html', **locals())   




# %% California
@app.route('/California')
def California():
    California = r3.json()
    cityName = California['name']
    country= California['sys']['country']
    localtime = California['timezone']    
    cityLongitud = California['coord']['lon']
    cityLatitud = California['coord']['lat']
    temp_K  = California['main']['temp'] -273
    humidity = California['main']['humidity']
    pressure = 0.0295*California['main']['pressure']    
    wind_speed = California['wind']['speed']

    return render_template('California.html', **locals())  



# %% Toronto
@app.route('/Toronto')
def Toronto():
    Toronto = r4.json()
    cityName = Toronto['name']
    country= Toronto['sys']['country']
    localtime = Toronto['timezone']    
    cityLongitud = Toronto['coord']['lon']
    cityLatitud = Toronto['coord']['lat']
    temp_K  = Toronto['main']['temp'] -273
    humidity = Toronto['main']['humidity']
    pressure = 0.0295*Toronto['main']['pressure']    
    wind_speed = Toronto['wind']['speed']

    return render_template('Toronto.html', **locals())      






if __name__ == "__main__":
    app.run()