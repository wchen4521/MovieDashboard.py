"""
INST326 Final Project

Authors: Haaris Malik, Jacob Levy

This code is for pulling data from the IMDB API and letting a user enter the name of any movie,
then the code pulls all the info of that movie that has been searched by the user.
"""
import requests  

def movie_options(KEY, movie_name):
    """ Retrives the list of IMDB movie IDs a user may get when searching a title.
    Args:
        KEY (string): The API key.
        movie_name (string): The name of the movie.
    Returns:
        movie_ids (list): The IDs of each movie. 
        movie_names (list): The corresponding name of each movie.
    """
    #Searching movies by name. This can bring up multiple movies I.E. Superman can bring up Superman 1/2/3, Man of Steel, etc.
    url = f"https://imdb-api.com/en/API/SearchMovie/{KEY}/{movie_name}"
    response = requests.request("GET", url)
    print(response.json())

    movie_ids = []
    #Gathering the IDs from our response and appending them to our list.
    for movie_entry in response.json()['results']:
        movie_ids.append(movie_entry['id'])

    movie_names = []
    #Gathering the names from our response and appending them to our list.
    for movie_entry in response.json()['results']:
        movie_names.append(movie_entry['title'])

    return movie_ids, movie_names

def chosen_movie(KEY, id):
    """ Searches the movie by its exact IMDB ID, which returns a detailed response from the API.
    Args:
        KEY (string): The API key.
        id (string): The ID of the movie.
    Returns:
        response (): The requests response object
    """
    url = f"https://imdb-api.com/en/API/Title/{KEY}/{id}/FullCast,Ratings,Wikipedia,"
    response = requests.request("GET", url)
    return response

