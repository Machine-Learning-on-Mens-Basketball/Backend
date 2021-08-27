from flask import request, current_app as app
from flask_restful import Resource, request

from app.main.services.make_prediction_service import MakePredictionService

#Prediction endpoint
class PredictController(Resource):
    def __init__(self):
        pass

    #Make a prediction
    def get(self):
        team1 = request.args.get('team1')
        team2 = request.args.get('team2')
        prediction = MakePredictionService()
        return prediction.make_prediction(team1, team2)