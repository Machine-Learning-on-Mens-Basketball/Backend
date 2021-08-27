from flask import current_app as app
from flask import jsonify, Flask, Response
from app.main.exceptions.mlmb_exception import MlmbException

app = Flask(__name__)
with app.app_context():
    class InvalidTeamException(MlmbException):
        @app.errorhandler(MlmbException)
        def handle_invalid_team_exception(self, error):
            with app.app_context():
                error = 1
                message = "The team(s) provided were not valid"
                app.logger.warn("error: " + error + " message: " + message)
                return (
                    Response(
                        jsonify(
                            {
                                'error': error,
                                'message': message
                            }
                        ), 
                        status=400, 
                        mimetype='application/json'
                    )
                )
                    