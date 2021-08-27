from app.main.exceptions.invalid_team_exception import InvalidTeamException
from app.main.models.prediction_model_DAO import PredictionModelDAO
from app.main.models.prediction_response_DTO import PredictionResponseDTO

class PredictionModelService():

    def __init__(self):
        pass

    #Service for making a prediction
    def get_model_prediction(self, team1, team2):
        if team1 == None or team2 == None:
            return InvalidTeamException
        else:
            new_prediction = PredictionModelDAO()
            new_prediction.set_team1_name(team1)
            new_prediction.set_team2_name(team2)
            #Need to implement prediction models here...
            #Returning fake results for now...
            result_prediction = PredictionResponseDTO()
            result_prediction.set_team1_name(team1)
            result_prediction.set_team2_name(team2)
            result_prediction.set_team1_percent("0%")
            result_prediction.set_team2_percent("100%")
            return result_prediction.generate_response()