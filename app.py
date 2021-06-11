from helpers import getTeams
from flask import Flask, escape, request
from predictor import Predictor

# Commenting Flask for PythonAnywhere
# https://help.pythonanywhere.com/pages/Flask
# app = Flask(__name__)

# PythonAnywhere requires this import
import sys
path = '/home/reyesrico/49ers-predictor'
if path not in sys.path:
   sys.path.insert(0, path)

from flask_app import app as application


white = ['http://localhost:8080','http://localhost:3000', 'http://localhost:5000']

@app.after_request
def add_cors_headers(response):
    # r = request.referrer[:-1]
    # if r in white:
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Headers', 'Cache-Control')
    response.headers.add('Access-Control-Allow-Headers', 'X-Requested-With')
    response.headers.add('Access-Control-Allow-Headers', 'Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')
    return response

# HELLO WORLD
@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return 'Hello, ' + escape(name)

@app.route('/teams', methods=['GET'])
def teams():
  return { 'teams': getTeams() }

# PREDICT
# http://localhost:5000/predict?team_number=11&week_number=3&is_playoff=0&is_super_bowl=0&is_local=1&weather_wind=1&weather_humidity=52
@app.route('/predict', methods=['GET'])
def predict():
  teamNumber = request.args.get('team_number', '')
  weekNumber = request.args.get('week_number', '')
  isPlayoff = request.args.get('is_playoff', '')
  isSuperBowl = request.args.get('is_super_bowl', '')
  is49ersLocal = request.args.get('is_local', '')
  weatherWindMPH = request.args.get('weather_wind', '')
  weatherHumidity = request.args.get('weather_humidity', '')

  pred = Predictor()
  pred.generateData()
  pred.trainData()
  result = pred.predict(teamNumber, weekNumber, isPlayoff, isSuperBowl, is49ersLocal, weatherWindMPH, weatherHumidity)
  print('Super result!!! => ' + str(result))

  return {
    "predict": result
  }
