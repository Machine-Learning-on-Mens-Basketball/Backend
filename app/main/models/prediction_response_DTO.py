class PredictionResponseDTO():

    team1_name = None
    team2_name = None
    team1_percent = None
    team2_percent = None

    def get_team1_name(self):
        return self.team1_name

    def get_team2_name(self):
        return self.team2_name

    def get_team1_percent(self):
        return self.team1_percent

    def get_team2_percent(self):
        return self.team2_percent

    def set_team1_name(self, name):
        self.team1_name = name

    def set_team2_name(self, name):
        self.team2_name = name
    
    def set_team1_percent(self, percent):
        self.team1_percent = percent
    
    def set_team2_percent(self, percent):
        self.team2_percent = percent

    def generate_response(self):
        data = {
                'code': 0,
                'message': "Successfully made test prediction",
                'payload': {
                    'team1Name': self.team1_name,
                    'team2Name': self.team2_name,
                    'team1Precent': self.team1_percent,
                    'team2Percent': self.team2_percent
                }
        }
        return(data, 200)