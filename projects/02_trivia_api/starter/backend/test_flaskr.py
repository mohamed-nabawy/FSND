import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format('postgres:123456@localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_creating_question(self):
        """Test creating a new question """
        body = {'question':'new question', 'answer':'new answer', 'category':2, 'difficulty': 5}
        res = self.client().post('http://localhost:5000/api/questions', data=json.dumps(body), headers={'Content-Type': 'application/json'})
        self.assertEqual(res.status_code, 200)

    def test_creating_question_error(self):
        """Test creating a new question """
        body = {'question':'new question', 'answer':'', 'category':5, 'difficulty': 5}
        res = self.client().post('http://localhost:5000/api/questions', data=json.dumps(body), headers={'Content-Type': 'application/json'})
        self.assertEqual(res.status_code, 422)

    def test_deleting_question(self):
        """Test deleting a question """
        res = self.client().delete('http://localhost:5000/api/questions/6')
        self.assertEqual(res.status_code, 200)

    def test_deleting_question_error(self):
        """Test deleting a question """
        res = self.client().delete('http://localhost:5000/api/questions/s')
        self.assertEqual(res.status_code, 404)    

    def test_searching_questions(self):
        """Test searching a question """
        body = {'searchTerm':'is'}
        res = self.client().post('http://localhost:5000/api/questions/search', data=json.dumps(body), headers={'Content-Type': 'application/json'})
        self.assertEqual(res.status_code, 200)

    def test_searching_questions_error(self):
        """Test searching a question """
        body = {'searchTerm':'isssss'}
        res = self.client().post('http://localhost:5000/api/questions/search', data=json.dumps(body), headers={'Content-Type': 'application/json'})
        self.assertEqual(res.status_code, 404)

    def test_fetching_questions(self):
        """Test fetching questions """
        res = self.client().get('http://localhost:5000/api/questions')
        self.assertEqual(res.status_code, 200)

    def test_fetching_questions_error(self):
        """Test fetching questions """
        res = self.client().get('http://localhost:5000/api/questionsaaaa')
        self.assertEqual(res.status_code, 404)

    def test_fetching_categories(self):
        """Test fetching categories """
        res = self.client().get('http://localhost:5000/api/categories')
        self.assertEqual(res.status_code, 200)

    def test_fetching_categories_error(self):
        """Test fetching categories """
        res = self.client().get('http://localhost:5000/api/categoriesbbbbbb')
        self.assertEqual(res.status_code, 404)

    def test_fetching_category_questions(self):
        """Test fetching categories """
        res = self.client().get('http://localhost:5000/api/categories/1/questions')
        self.assertEqual(res.status_code, 200)

    def test_fetching_category_questions_error(self):
        """Test fetching categories """
        res = self.client().get('http://localhost:5000/api/categories/aa/questions')
        self.assertEqual(res.status_code, 404)

    def test_getting_question_from_quizz(self):
        """Test getting question from quizz """
        body = {'previous_questions':[], 'quiz_category':{'id':2}}
        res = self.client().post('http://localhost:5000/api/quizzes', data=json.dumps(body), headers={'Content-Type': 'application/json'})
        self.assertEqual(res.status_code, 200)    

    def test_getting_question_from_quizz_error(self):
        """Test getting question from quizz """
        body = {'previous_questions':[], 'quiz_category':5}
        res = self.client().post('http://localhost:5000/api/quizzes', data=json.dumps(body), headers={'Content-Type': 'application/json'})
        self.assertEqual(res.status_code, 422)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()