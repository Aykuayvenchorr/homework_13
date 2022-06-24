from flask import Flask, Blueprint, jsonify
from utils import search_movie, range_years, the_latest_movies, the_rate_movies

bp_movies = Blueprint('bp_movies', __name__)


@bp_movies.route('/')
def main_page():
    return 'Главная страница'


@bp_movies.route('/movie/<title>/')
def show_film_data(title):
    movie = search_movie(title)
    return movie


@bp_movies.route('/movie/<year_1>/to/<year_2>/')
def range_films(year_1, year_2):
    result = range_years(year_1, year_2)
    return jsonify(result)


@bp_movies.route('/rating/children/')
def children_film():
    movies = the_rate_movies('children')
    return jsonify(movies)


@bp_movies.route('/rating/family/')
def family_film():
    movies = the_rate_movies('family')
    return jsonify(movies)


@bp_movies.route('/rating/adult/')
def adult_film():
    movies = the_rate_movies('adult')
    return jsonify(movies)


@bp_movies.route('/genre/<genre>/')
def show_the_latest_movies_genre(genre):
    result = the_latest_movies(genre)
    return jsonify(result)


