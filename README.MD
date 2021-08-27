# MLMB Backend

## Purpose
This app will handle all of the requests from the front end and call upon the defined services. This is all written in Python using the Flask framework to match our data science team who uses Python libraries for their modeling.

## Getting Started
### Requirements
* Python 3.*
* Any IDE (VSCode prefered)
### How to Start
1. Open the root app directory in a terminal and run the following to install all dependencies:
`pip install -r requirements.txt --user`
2. From the root folder, run the following to start the app: `python manage.py`

## Testing
There is only one test service running that returns a preset value. To test, run the app and use the following url: `http://127.0.0.1:5000/predict?team1=blank&team2=blank` replacing the blanks with names of teams. If the query is successful, it should return a 0 code, a message, and the given payload.

## Principle Practices
The architecture of this app follows the following design patterns/rules:
* REST
* Microservices
* MVC

## Functionality
Following the principles defined above, we typically have the controller be the entry point for a request. The controller will call upon a service to perform an action and return a response back to the controller, which the controller will then return that response to the user. Models are objects defined to provide clarity and safety. They make sure we get/send exactly what we want and can handle errors with our custom exceptions when that is not the case. When it comes to models, we typically have DAOs that deal with database interactions. We also have DTOs, which are used transfer our objects between different interfaces/services/processes internally or externally.

## Standards
This app tries to follow industry standard as far as implementation goes. The following are key points that will be delivered upon during this project:
- [ ] Logging
- [ ] Exceptions
- [ ] Tests
- [ ] Comments
- [ ] Documentation

## Author
Brandon Mino