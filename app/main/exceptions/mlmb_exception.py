class MlmbException(Exception):

    def __init__(self, app_error_code, message):
        self.app_error_code = app_error_code
        self.message = message

    # def __str__(self):
    #     return f'{self.app_error_code} -> {self.message}'