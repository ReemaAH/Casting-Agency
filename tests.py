import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import *


class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the CastingAgency test cases"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "castingAgency_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
    

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
        
        # # setup roles headers
        # self.casting_assistant = {
        #     'Authorization': 'Bearer ' + os.environ.get('ASSISTANT_TOKEN')}
        # self.casting_director = {
        #     'Authorization': 'Bearer ' + os.environ.get('DIRECTOR_TOKEN')}
        # self.executive_producer = {
        #     'Authorization': 'Bearer ' + os.environ.get('PRODUCER_TOKEN')}

         # setup roles headers
        self.casting_assistant = {
            'Authorization': 'Bearer ' + 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVKdkV3UmZWbW1FYnNkb1puWmVKRSJ9.eyJpc3MiOiJodHRwczovL2Nhc3RpbmctYWdlbmN5LWZzZG4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmZGRmYzkwYmJjNGY5MDA2ZjFmNGEyMiIsImF1ZCI6ImF1dGgiLCJpYXQiOjE2MDgzODk2NjEsImV4cCI6MTYwODM5Njg2MSwiYXpwIjoid3lMZnY5QXBJT3RhU1FlN2s1b2I3M2QyN21wbjdNdVciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.WGqhQQC8fhN9JBBnqMH1KVeow28w52qKoZee_16Rde6MJ1Om0uHu4MS39hqvWNGYr8dbLUKn9tW2U5KDcbekyJTApLKDuJRK2i-dcg0urdH833szc2UBLj4zq90zzvY57npe3mGZ2L6V4RKqqNz1gQKQ4xN0ZbEo0ql6douHxekIQBKdRySEsqZuYZPSBiwnTY_YiBB9L7-BJYrwlUr9A92hnhnKv9b0mYCJfyJ7G85_B6nLjOgh7M-KOVY1-Gi-OJ-05Vi6-6gkJy1s9-ZyTwDXpS2d4ZQTaPJZtZQNTpKzxruSVw85WafjRnuJupy42RMXXrik8FaoOds12yf7vw'}
        self.casting_director = {
            'Authorization': 'Bearer ' + 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVKdkV3UmZWbW1FYnNkb1puWmVKRSJ9.eyJpc3MiOiJodHRwczovL2Nhc3RpbmctYWdlbmN5LWZzZG4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmZGRlZjczZTAwYTgzMDA2ZTg4ZjNjZiIsImF1ZCI6ImF1dGgiLCJpYXQiOjE2MDgzODE2MTEsImV4cCI6MTYwODM4ODgxMSwiYXpwIjoid3lMZnY5QXBJT3RhU1FlN2s1b2I3M2QyN21wbjdNdVciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.G_QWD0xtdsgR2yP6YXpcZgYeajZRtfujSy4z48RIDgcw5zw5nQCqsmpQb3U9P3IiWg5CNzmaYQg5L5fHsbJaAEdE8hC1uur6vAHOfqBG86THSt9llQ12jPLmGYdgmMPgW8nCnG4wU3aoNiU-2sY0d1fE9NQTYa7S7nRRWTDn_BnbLyQKazES7mGdNUbCB4DKts9FbKbd78e9_5vbp_FBDFaxb7XO5knoV9Q3y5tklU2d7_3B3n3Eb0H0xtToY5el98F-wZ3lWvgAH0XM-2d8sTuHHp4Cxj-44Mi2gpRz-V7ffFX8Ip7FO2qhJPsezOf3Of1V2TmOXpUaGh1V7-PsWQ'}
        self.executive_producer = {
            'Authorization': 'Bearer ' + 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVKdkV3UmZWbW1FYnNkb1puWmVKRSJ9.eyJpc3MiOiJodHRwczovL2Nhc3RpbmctYWdlbmN5LWZzZG4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmZGRlZmI3NDUyMjY4MDA3NTU5ZDBiOCIsImF1ZCI6ImF1dGgiLCJpYXQiOjE2MDgzODk5NDYsImV4cCI6MTYwODM5NzE0NiwiYXpwIjoid3lMZnY5QXBJT3RhU1FlN2s1b2I3M2QyN21wbjdNdVciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.q2P15G6Qx6k2ajltbOWvnVbWbYbUnY-rkZvWQ5fzWYikyScxHeE0wfBNOK7NLf554B7f_HS4LpmDgrM8CuW7QMU_NoyHicysBYz8N2YP9-1TRxCmF3iEV8ocDvFAQb2cX2wmtOw_rrFvHIB3LWhpNJwzQYau0MtV-3WFKJM6KL57Y7dhH9jTd2ySJvXhh3EAr08OCfO4IpDFNa_KVmDAYvc754QCAeCB8k1X1-9MN7leb9s8Say9wriU-muE1B026alpF40fMqeFfaqmNBjkYePE9SXmVPyXUVkDNGvKiN-15Ecq-_Bv2QLZKWFWQpykgEYpVNvhNt9LO7Nv2xA7YQ'}




    def tearDown(self):
        """Executed after reach test"""
        pass


    def test_get_actors_success(self):
        """ Test get actors success """
        ## create a new obj
        actor_test = Actor(
        name='Reema', 
        age=23, 
        gender='female')
        actor_test.insert()

        # get response data
        response = self.client().get('/actors', headers= self.casting_assistant)
     

        ## check success value, status_code and if there is an actors list
        self.assertTrue(json.loads(response.data)['success'])
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(json.loads(response.data)['actors']))


    def test_get_actors_failure(self):
        """ Test get actors failure """
        ## get response data when there are no actors in DB
        db.session.query(Actor).delete()
        db.session.commit()
        response = self.client().get('/actors', headers=self.casting_assistant)
        ## 404 since no actors are stored in DB
        self.assertEqual(response.status_code, 404)


    def test_get_actors_unauthorized(self):
        """ Test get actors failure """
        ## get response data when there are no actors in DB
        db.session.query(Actor).delete()
        db.session.commit()
        response = self.client().get('/actors')
        ## Unauthorized since no header was provided 
        self.assertEqual(response.status_code, 401)


    def test_get_movies_success(self):
        """ Test get movies success """
        ## create a new obj
        movie_test = Movie(
        title='title', 
        release_date="Sat, 16 Apr 1997 12:45:00 GMT")
        movie_test.insert()
        
        # get response data + adding headers
        response = self.client().get('/movies', headers=self.casting_assistant)

        ## check success value, status_code and if there is an actors list
        self.assertTrue(json.loads(response.data)['success'])
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(json.loads(response.data)['movies']))


    def test_get_movies_failure(self):
        """ Test get movies failure """
        ## get response data when there are no actors in DB
        db.session.query(Movie).delete()
        db.session.commit()
        response = self.client().get('/movies', headers=self.casting_assistant)
        ## since there are no movies in the DB the error code will be 404
        self.assertEqual(response.status_code, 404)
    

    def test_get_movies_unauthorized(self):
        """ Test get movies failure """
        ## get response data when there are no actors in DB
        db.session.query(Movie).delete()
        db.session.commit()
        response = self.client().get('/movies')
        ## unauthorized since no header was provided in the request
        self.assertEqual(response.status_code, 401)

    
    def test_delete_actor_success(self):
        """ Test delete actor success """
        ## create a obj
        actor_test = Actor(
        name='Reema', 
        age=23, 
        gender='female')
        actor_test.insert()
        ## get the number of actors before deleting the obj
        actors_total_before = len(Actor.query.all())
        ## send request to delete the newely created obj 
        response = self.client().delete('/actors/'+ format(actor_test.id),
                                        headers=self.casting_director)
        ## get the number of actors after deleting the obj
        actors_total_after = len(Actor.query.all())

        ## check success value, status_code 
        self.assertTrue(json.loads(response.data)['success'])
        self.assertEqual(response.status_code, 200)
        ## compare actors_total_before and actors_total_after to check if the obj deleted 
        self.assertFalse(actors_total_before == actors_total_after)
        self.assertTrue(actors_total_before > actors_total_after)
    

    def test_delete_actor_failure(self):
        """ Test delete actor failure """
        ## get response data
        response = self.client().delete('/actors/'+ format(100),
                                        headers=self.casting_director)

        ## check success value, status_code 
        self.assertFalse(json.loads(response.data)['success'])
        self.assertEqual(response.status_code, 422)


    def test_delete_actor_unauthorized(self):
        """ Test delete actor failure """
        ## get response data
        response = self.client().delete('/actors/'+ format(100),
                                        headers=self.casting_assistant)

        ## check success value, status_code 
        self.assertFalse(json.loads(response.data)['success'])
        # 401 since the casting_assistant is unauthorized to delete an actor
        self.assertEqual(response.status_code, 401)
    

    def test_delete_movie_success(self):
        """ Test delete movie success """

        ## create a obj
        movie_test = Movie(
        title='title', 
        release_date="Sat, 16 Apr 1997 12:45:00 GMT")
        movie_test.insert()

        ## get the number of movies before deleting the obj
        movies_total_before = len(Movie.query.all())
        ## send request to delete the newely created obj 
        response = self.client().delete('/movies/'+ format(movie_test.id),
                                        headers=self.executive_producer)
        ## get the number of movies after deleting the obj
        movies_total_after = len(Movie.query.all())

        ## check success value, status_code 
        self.assertTrue(json.loads(response.data)['success'])
        self.assertEqual(response.status_code, 200)
        ## compare actors_total_before and actors_total_after to check if the obj deleted 
        self.assertFalse(movies_total_before == movies_total_after)
        self.assertTrue(movies_total_before > movies_total_after)


    def test_delete_movie_failure(self):
        """ Test delete movie failure """
        ## get response data
        response = self.client().delete('/movies/'+ format(100), 
                                        headers=self.executive_producer)

        # 422 since the provided ID is wrong
        self.assertEqual(response.status_code, 422)
    

    def test_delete_movie_unauthorized(self):
        """ Test delete movie failure """
        ## get response data
        response = self.client().delete('/movies/'+ format(100), 
                                        headers=self.casting_director)

        # Unauthorized since the casting_director 
        # doesn't have permission to delete an actor
        self.assertEqual(response.status_code, 401)
    

    def test_create_new_actor_success(self):
        """ Test create a actor obj success """
        ## get the number of actors before creating a new obj
        actors_total_before = len(Actor.query.all())

        ## create a new obj
        actor_test = Actor(
        name='Reema', 
        age=23, 
        gender='female')
        
        ## load response data
        response = self.client().post('/actors', json=actor_test.format(),
                                      headers=self.casting_director)
     
        ## get the number of actors after creating a new obj
        actors_total_after = len(Actor.query.all())

        ## check success value, status_code 
        self.assertTrue(json.loads(response.data)['success'])
        self.assertEqual(response.status_code, 200)

        ## compare actors_total_before and actors_total_after to check if the obj deleted 
        self.assertFalse(actors_total_before == actors_total_after)
        self.assertTrue(actors_total_before < actors_total_after)
    

    def test_create_actor_failure(self):
        """ Test create actor obj failure """
        ## get the number of actors after creating a new obj
        actors_total_before = len(Actor.query.all())

        ## load response data
        response = self.client().post('/actors', json={},
                                      headers=self.casting_director)
    
        ## get the number of actors after creating a new obj
        actors_total_after = len(Actor.query.all())
        
        ## 422 since not data was provided in the request
        self.assertEqual(response.status_code, 422)
        ## as no obj was created the actors_total_before should be equal actors_total_after
        self.assertTrue(actors_total_before == actors_total_after)


    def test_create_actor_unauthorized(self):
        """ Test create actor obj unauthorized """
        ## get the number of actors after creating a new obj
        actors_total_before = len(Actor.query.all())
        actor_test = Actor(
        name='Reema', 
        age=23, 
        gender='female')

        ## load response data
        response = self.client().post('/actors', json=actor_test.format(),
                                      headers=self.casting_assistant)
    
        ## get the number of actors after creating a new obj
        actors_total_after = len(Actor.query.all())
        
        # Unauthorized since the casting_director 
        # doesn't have permission to delete an actor
        self.assertEqual(response.status_code, 401)
        ## as no obj was created the actors_total_before should be equal actors_total_after
        self.assertTrue(actors_total_before == actors_total_after)
    

    def test_create_movie_success(self):
        """ Test create a movie obj success """
        ## get the number of movies before creating a new obj
        movies_total_before = len(Movie.query.all())

        ## create a new obj
        movie_test = Movie(
        title='title', 
        release_date="Sat, 16 Apr 1997 12:45:00 GMT")
        
        ## load response data
        response = self.client().post('/movies', json=movie_test.format(),
                                      headers=self.executive_producer)
     
        ## get the number of movies after creating a new obj
        movies_total_after = len(Movie.query.all())

        ## status_code 
        self.assertEqual(response.status_code, 200)

        ## compare movies_total_before and movies_total_after to check if the obj deleted 
        self.assertFalse(movies_total_before == movies_total_after)
        self.assertTrue(movies_total_before < movies_total_after)
    

    def test_create_movies_failure(self):
        """ Test create movie obj failure """
        ## get the number of actors after creating a new obj
        movies_total_before = len(Movie.query.all())
     
        ## load response data
        response = self.client().post('/movies', json={},
                                      headers=self.executive_producer)
    
        ## get the number of movies after creating a new obj
        movies_total_after = len(Movie.query.all())

        self.assertEqual(response.status_code, 422)
        ## as no obj was created the movies_total_before should be equal movies_total_after
        self.assertTrue(movies_total_before == movies_total_after)


    def test_create_movies_unauthorized(self):
        """ Test create movie obj unauthorized """
        ## get the number of actors after creating a new obj
        movies_total_before = len(Movie.query.all())
        movie_test = Movie(
        title='title', 
        release_date="Sat, 16 Apr 1997 12:45:00 GMT")

        ## load response data
        response = self.client().post('/movies', json=movie_test.format(),
                                      headers=self.casting_director)
    
        ## get the number of movies after creating a new obj
        movies_total_after = len(Movie.query.all())
        
        # 401 status_code since the casting_director 
        # doesn't have permission to create a movie
        self.assertEqual(response.status_code, 401)
        ## as no obj was created the movies_total_before should be equal movies_total_after
        self.assertTrue(movies_total_before == movies_total_after)


    def test_update_actor_success(self):
        """ Test update actor success """
        actor_test = Actor(
        name='name', 
        age=23, 
        gender='female')
        actor_test.insert()

        ## load response data
        response = self.client().patch('/actors/' + format(actor_test.id),
                                       json={'name': "name1"},
                                       headers=self.casting_director)
        # Load the data using json.loads of the response

        self.assertTrue(json.loads(response.data)['success'])
        self.assertEqual('name1', json.loads(response.data)['actor']['name'])
        self.assertEqual(response.status_code, 200)


    def test_update_actor_failure(self):
        """ Test update actor failure """

        ## send request with wrong actor ID
        response = self.client().patch('/actors/' + format(100),
                                     json={'name': "name1"},
                                     headers=self.casting_director)
        # Load the data using json.loads of the response
        self.assertEqual(response.status_code, 404)
    

    def test_update_actor_unauthorized(self):
        """ Test update actor unauthorized """

        ## send request with wrong actor ID
        response = self.client().patch('/actors/' + format(100),
                                     json={'name': "name1"},
                                     headers=self.casting_assistant)
        # Load the data using json.loads of the response
        # 401 status_code since the casting_assistant
        # doesn't have permission to create a movie
        self.assertEqual(response.status_code, 401)
    

    def test_update_movie_success(self):
        """ Test update movie success """
        movie_test = Movie(
        title='title', 
        release_date="Sat, 16 Apr 1997 12:45:00 GMT")
        movie_test.insert()

        ## load response data
        response = self.client().patch('/movies/' + format(movie_test.id),
                                     json={'title': "title1"},
                                     headers=self.executive_producer)
        # Load the data using json.loads of the response
        self.assertTrue(json.loads(response.data)['success'])
        self.assertEqual('title1', json.loads(response.data)['movie']['title'])
        self.assertEqual(response.status_code, 200)


    def test_update_movie_failure(self):
        """ Test update movie failure """

        ## load response data
        response = self.client().patch('/movies/' + format(100),
                                     json={'title': "title1"},
                                     headers=self.executive_producer)
        # Load the data using json.loads of the response
        self.assertEqual(response.status_code, 404)


    def test_update_movie_unauthorized(self):
        """ Test update movie unauthorized """

        ## load response data
        response = self.client().patch('/movies/' + format(100),
                                     json={'title': "title1"},
                                     headers=self.casting_assistant)

        # Load the data using json.loads of the response
        # 401 status_code since the casting_assistant
        # doesn't have permission to create a movie
        self.assertEqual(response.status_code, 401)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()