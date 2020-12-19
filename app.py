import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth import AuthError, requires_auth
from models import *
import random


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  # to setup the database
  setup_db(app)
  CORS(app)

  '''
  Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
      response.headers.add('Access-Control-Allow-Headers',
                          'Content-Type,Authorization,true')
      response.headers.add('Access-Control-Allow-Methods',
                           'GET,PUT,POST,DELETE,OPTIONS')
      return response

  # Main endpoint
  @app.route('/')
  def index():
    return jsonify({
      'message': 'Casting Agency system'
        }), 200


  @app.route('/actors')
  @requires_auth('get:actors')
  # this endpoint to get all actors in the DB
  def get_actors(payload):
    actors = Actor.query.all()
    if len(actors) == 0:
            abort(404)
    else:
      actors = [actor.format() for actor in actors]
      return jsonify({
        'success': True,
        'actors': actors
        })


  @app.route('/movies')
  @requires_auth('get:movies')
  # this endpoint is to get all movies in DB
  def get_movies(payload):
    movies = Movie.query.all()
    if len(movies) == 0:
            abort(404)
    else:
      movies = [movie.format() for movie in movies]
      return jsonify({
        'success': True,
        'movies': movies
        })


  @app.route("/actors/<int:actor_id>", methods=['DELETE'])
  @requires_auth('delete:actors')
  # This endpoint is to delete an actor
  def delete_actor(payload, actor_id):
    try:
      actor = Actor.query.get(actor_id)
      actor.delete()
      return jsonify({
        'success': True,
        'deleted': actor_id
        })
    except:
      abort(422)
  

  @app.route("/movies/<int:movie_id>", methods=['DELETE'])
  @requires_auth('delete:movies')
  # This endpoint is to delete a movie
  def delete_movie(payload, movie_id):
    try:
      movie = Movie.query.get(movie_id)
      movie.delete()
      return jsonify({
        'success': True,
        'deleted': movie_id
        })
    except:
      abort(422)

  
  @app.route("/actors", methods=['POST'])
  @requires_auth('post:actors')
  # this endpoint it to create a new obj 
  # from post data
  def create_actor(payload):
    # validation
    if 'name' in request.get_json() and 'age' in request.get_json() \
      and 'gender' in request.get_json():
      name = request.get_json()['name']
      age = request.get_json()['age']
      gender = request.get_json()['gender']
  
      new_actor = Actor(
        name=name, 
        age=age, 
        gender=gender)
      new_actor.insert()

      return jsonify({
        'success': True,
        'created': new_actor.id
        })
    else:
      abort(422)
  

  @app.route("/movies", methods=['POST'])
  @requires_auth('post:movies')
  # this endpoint it to create a new obj 
  # from post data
  def create_movie(payload):
    # validation
    if 'title' in request.get_json() and 'release_date' in request.get_json():
      title = request.get_json()['title']
      release_date = request.get_json()['release_date']

      new_movie = Movie(
        title=title, 
        release_date=release_date)
      new_movie.insert()

      return jsonify({
        'success': True,
        'created': new_movie.id
        })
    else:
      abort(422)


  @app.route('/actors/<int:actor_id>', methods=['PATCH'])
  @requires_auth('patch:actors')
  def update_actor(payload, actor_id):
    try:
      actor = Actor.query.get(actor_id)
      # check if title in post data 
      if 'name' in request.get_json():
        name = request.get_json()['name']
        actor.name = name
      # check if name in post data 
      if 'age' in request.get_json():
        age = request.get_json()['name']
        actor.age = age
      # check if gender in post data 
      if 'gender' in request.get_json():
        gender = request.get_json()['gender']
        actor.gender = gender
 
      actor.update()
      return jsonify({'success': True, 'actor': actor.format() })
    
    except BaseException:     
      # if the object is not exist a 404 error will be returned
      abort(404)
  

  @app.route('/movies/<int:movie_id>', methods=['PATCH'])
  @requires_auth('patch:movies')
  def update_movie(payload, movie_id):
    try:
      movie = Movie.query.get(movie_id)
      # check if title in post data 
      if 'title' in request.get_json():
        title = request.get_json()['title']
        movie.title = title
      # check if release_date in post data 
      if 'release_date' in request.get_json():
        release_date = request.get_json()['release_date']
        movie.release_date = release_date

      movie.update()
      return jsonify({'success': True, 'movie': movie.format()})
    
    except BaseException:     
      # if the object is not exist a 404 error will be returned
      abort(404)

  ## errorhandler for 404
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
        "success": False, 
        "error": 404,
        "message": "Not found"
        }), 404


  ## errorhandler for 422
  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False, 
      "error": 422,
      "message": "unprocessable"
      }), 422


  # errorhandler for 500
  @app.errorhandler(500)
  def internal_server_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'Internal Server Error'
        }), 500


  # errorhandler for 401 (Unauthorized)
  @app.errorhandler(AuthError)
  def auth_error(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "Unauthorized",
    }), 401

  return app

app = create_app()

# Default port:
if __name__ == '__main__':
    app.debug = True
    app.run()

    