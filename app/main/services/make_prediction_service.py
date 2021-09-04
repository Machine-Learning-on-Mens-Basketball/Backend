from flask import Flask

import requests
from app.main.models.prediction_response_DTO import PredictionResponseDTO
from app.main.exceptions.invalid_team_exception import InvalidTeamException
from app.main.services.prediciton_model_service import PredictionModelService

app = Flask(__name__)
with app.app_context():
    class MakePredictionService():

        def __init__(self):
            pass

        #Service for making a prediction
        def make_prediction(self, team1, team2):
            app.logger.debug("Attempting to make a predicition")
            if team1 == None or team2 == None:
                return InvalidTeamException
            else:
                #Need to get predictions from models here
                new_prediction = PredictionResponseDTO()
                model_prediction = requests.get('http://localhost:7000/predictBasicModel?team1=' + team1 + '&team2=' + team2).json()
                app.logger.debug("Made prediction with following info: " + str(''.join(map(str, model_prediction))))
                return model_prediction
