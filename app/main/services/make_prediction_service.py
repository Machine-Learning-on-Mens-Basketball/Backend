from flask import Flask

from app.main.models.prediction_request_DTO import PredictionRequestDTO
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
                new_prediction = PredictionRequestDTO()
                new_prediction.set_team1_name(team1)
                new_prediction.set_team2_name(team2)
                
                model_prediction = PredictionModelService()
                result_prediction = model_prediction.get_model_prediction(team1, team2)
                app.logger.debug("Made prediction with following info: " + str(''.join(map(str, result_prediction))))
                return result_prediction
