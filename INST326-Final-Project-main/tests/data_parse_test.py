"""
INST326 Final Project Test Program

Author: Chen Wang, Jacob Levy

This program parses the data received from a json response. To be used in conjunction with the other programs in this directory.
"""
import requests

def parse_response(response):
    """ Takes the requests response we received, changes it to a json format, and parses it for relevant information.
    Args:
        response (requests object): The API response we received from IMDB API via the requests module.
    Returns
        movie (Movie class object): An instance of the Movie class, with attributes populated by the data we parsed from the json.
    """
    #Converting to json format so we can parse it like a dictionary.
    info_json = response.json()
    fullTitle = info_json['fullTitle']
    year = info_json['year']
    age_rating = info_json['contentRating']
    runtime = info_json['runtimeStr']
    imdb_rating = info_json['imDbRating']
    plot = info_json['plot']

    #We want to show the names of five actors in our program, so we'll make a loop and append the first five in the json.
    casting = []
    for i in range(5):
        casting.append(info_json['actorList'][i]['name'])

    money = info_json['boxOffice']['cumulativeWorldwideGross']
    genres = info_json['genres']

    #Creating a list and populating it with three similar titles to the movie in question. 
    similar_movies = []
    for i in range(3):
        similar_movies.append(info_json['similars'][i]['title'])

    #Making an instance of our movie class, then returning it.
    movie = Movie(fullTitle, year, age_rating, runtime, imdb_rating, plot, casting, money, genres, similar_movies)

    return movie

class Movie:
    """ A class for a single movie. 
    Attributes:
        fullTitle (string): The name of the movie.
        year (int): The year it released.
        age_rating (string): It's recommended age rating E.G. PG-13.
        runtime (string): How long the movie is.
        imdb_rating (float): IMDB's rating for the movie's quality.
        plot (string): A plot synopsis.
        casting (list): The top five actors of the movie.
        money (float): The money it grossed, worldwide. 
        genres (string): The genres it's part of E.G. Action, Adventure.
        similar_movies (list): A list of similar titles to the movie. 
    """
    def __init__(self, fullTitle, year, age_rating, runtime, imdb_rating, plot, casting, money, genres, similar_movies):
        self.fullTitle = fullTitle
        self.year = year
        self.age_rating = age_rating
        self.runtime = runtime
        self.imdb_rating = imdb_rating
        self.plot = plot
        self.casting = casting
        self.money = money
        self.genres = genres
        self.similar_movies = similar_movies
