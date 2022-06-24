import sqlite3


def search_movie(movie):
    """Функция принимает название и возвращает данные о фильме"""

    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    movie_query = f"""
                    SELECT title, country, release_year, listed_in, description
                    FROM netflix
                    WHERE title LIKE '%{movie}%'
                    ORDER BY release_year desc
                    LIMIT 1
    """
    cur.execute(movie_query)
    executed_movie = cur.fetchall()
    movie_title = executed_movie[0]
    con.close()

    movie_data = {
        "title": movie_title[0],
        "country": movie_title[1],
        "release_year": movie_title[2],
        "genre": movie_title[3],
        "description": movie_title[4],
    }
    return movie_data


def range_years(start, finish):
    """Функция принимает диапазон лет и возвращает фильмы, снятые в эти года"""

    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    range_query = f"""
                    SELECT title, release_year
                    FROM netflix
                    WHERE release_year BETWEEN {start} AND {finish}
                    LIMIT 100
    """
    cur.execute(range_query)
    executed_query = cur.fetchall()
    movies = executed_query
    con.close()
    movies_data = []
    for movie in movies:
        movies_data.append({"title": movie[0], "release_year": movie[1]})

    return movies_data


def the_rate_movies(rate):
    """Функция принимает рейтинг и возвращает фильмы"""

    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    rate_system = {'children': ['G', 'G', 'G'], 'family': ['G', 'PG', 'PG-13'], 'adult': ['R', 'NC-17', 'R']}
    for key, value in rate_system.items():
        if rate == key:
            acceptable_rate = value
    rate_query = f"""
    SELECT title, rating, description
    FROM netflix
    WHERE rating = '{acceptable_rate[0]}' OR rating = '{acceptable_rate[1]}' OR rating = '{acceptable_rate[2]}'
    """
    cur.execute(rate_query)
    executed_rate = cur.fetchall()
    con.close()
    rate_data = []
    for movie in executed_rate:
        rate_data.append({"title": movie[0], 'rating': movie[1], "description": movie[2]})

    return rate_data


def the_latest_movies(genre):
    """Функция принимает жанр и возвращает фильмы этого жанра"""

    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    latest_query = f"""
    SELECT title, description
    FROM netflix
    WHERE listed_in LIKE '%{genre}%'
    """
    cur.execute(latest_query)
    executed_latest = cur.fetchall()
    con.close()
    movies_data = []
    for movie in executed_latest:
        movies_data.append({"title": movie[0], "description": movie[1]})

    return movies_data


def get_actors(one, two):
    """Функция принимает имена двух актеров и возвращает список тех, кто играет с ними в паре больше 2 раз"""

    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    actors_query = f"""
        SELECT "cast"
        FROM netflix
        WHERE "cast" LIKE '%{one}%' AND "cast" LIKE '%{two}%'
        """
    cur.execute(actors_query)
    executed_actors = cur.fetchall()
    con.close()
    list_of_actors = []
    for i in executed_actors:
        for j in i:
            list_of_actors.append(j)
    new = ', '.join(list_of_actors)
    new_list = new.split(', ')

    result = set()
    for actor in new_list:
        num = new_list.count(actor)
        if actor != one and actor != two and num > 2:
            result.add(actor)

    return result

# print(get_actors('Rose McIver', 'Ben Lamb'))

def type_year_genre(type, release_year, genre):
    """Функция принимает тип, год и жанр фильмы и возвращает фильмы"""

    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    type_query = f"""
    SELECT title, description
    FROM netflix
    WHERE type LIKE '%{type}%' AND release_year LIKE '{release_year}' AND listed_in LIKE '%{genre}%'
    """
    cur.execute(type_query)
    executed_type = cur.fetchall()
    con.close()
    return executed_type

# print(type_year_genre('TV Show', '2019', 'Reality TV'))
