# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET ...
POST ...
DELETE ...

GET '/api/categories'
- Fetches an array of categories and each category is a dictionary in which there is a key for the id and one for the value that is the corresponding string of the category
- Request Arguments: None
- Returns: An object with some keys: categories that contains an array of category objects of {id, type} and success: for indicating that request is handled correctly if true and false if otherwise.
{
    'success': True,
    'categories':[
                {'id':'1', 'type' : "Science"},
                {'id':'2', 'type' : "Art"},
                {'id':'3' , 'type' : "Geography"},
                {'id':'4' , 'type' : "History"},
                {'id':'5' , 'type': "Entertainment"},
                {'id':'6' , 'type': "Sports"}
                ]
}


GET '/api/questions?page=1'
- Fetches an array of all available questions in which each question is a dictionary that has keys for the question and one for the answer, category and the difficulty level and all available categories in which each category a dictionary that has a key for the id and one for the value that is the corresponding string of the category and total_questions which indicates the total number of stored questions.
- Request Arguments: page used for pagination i.e. /api/questions?page=1 to get the first page of questions that has 10 questions at max.
- Returns: An object with some keys: categories that contains an array of category objects, questions that has an array of questions objects, total_questions contains the count of all stored questions, success: for indicating that request is handled correctly if true and false if otherwise.
{
    'success': True,
    'categories': [
                {'id':'1', 'type' : "Science"},
                {'id':'2', 'type' : "Art"},
                ],
    'questions': [
                {'id':'1', 'question':'what is the color of sky', 'answer':'blue',  'category' : 'Science', 'difficulty':1},
                ],
    'total_questions': 15
}


POST '/api/questions'
- creates a new question that has keys for the question and one for the answer, category and the difficulty level.
- Request Arguments: the following body structure as json object: 
{ 
'question':'question title',
'answer':'answer text',
'category': 5,
'difficulty': 1
}.
- Returns: An object with a single key: success for indicating that request is handled correctly if true and false if otherwise.
{
    'success': True,
}


POST '/api/questions/search'
- searches questions titles using a word(color).
- Request Arguments: the following body structure as json object: 
{ 
'searchTerm':'color',
}.
- Returns: An object with some keys: questions that has an array of questions objects that contains the search term or word, total_questions contains the count of search result questions, success: for indicating that request is handled correctly if true and false if otherwise.
{
    'success': True,
    'questions': [ {'id':'1', 'question':'what is the color of sky', 'answer':'blue',  'category' : 'Science', 'difficulty':1},],
    'total_questions': 5,
}


GET '/api/categories/<category>/questions?page=1'
- Fetches an array of a specific category questions in which each question is a dictionary that has keys for the question and one for the answer, category and the difficulty level and all available categories in which each category a dictionary that has a key for the id and one for the value that is the corresponding string of the category and total_questions which indicates the total number of stored questions.
- Request Arguments: category for category id and page used for pagination i.e. /api/categories/<category>/questions?page=1 to get the first page of questions that has 10 questions at max.
- Returns: An object with some keys: questions that has an array of questions objects, total_questions contains the count of all stored questions, success: for indicating that request is handled correctly if true and false if otherwise.
{
    'success': True,
    'questions': [
                {'id':'1', 'question':'what is the color of sky', 'answer':'blue',  'category' : 'Science', 'difficulty':1},
                ],
    'total_questions': 15
}


POST '/api/quizzes'
- gets a random question from all stored questions or a specific categories and not a one from the previous questions passed as a parameter in the request.
- Request Arguments: the following body structure as json object: previous_questions is a list of all previous questions that user answered before in the quiz and quiz_category is the id of the category to get the questions from and if it's value is 0 the question is returned randomly from any category.
{ 
'previous_questions': [5, 6, 7],
'quiz_category': 0
}.
- Returns: An object with some keys: question that has a question object, success: for indicating that request is handled correctly if true and false if otherwise.
{
    'success': True,
    'question': {'id':'1', 'question':'what is the color of sky', 'answer':'blue',  'category' : 'Science', 'difficulty':1}
}

Errors:

in case of a bad request sent to any of the api endpoints, it will respond with a 400 status code and body with the following json object:
{
    "success": False, 
    "error": 400,
    "message": "Bad request"
}


in case of a request sent to any of the api endpoints and it's not exist, it will respond with a 404 status code and body with the following json object:
{
    "success": False, 
    "error": 404,
    "message": "Not found"
}


in case of a request sent to any of the api endpoints and it's not processable on the server, it will respond with a 422 status code and body with the following json object:
{
    "success": False, 
    "error": 422,
    "message": "Unprocessable request"
}

```


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```