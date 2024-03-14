"""
INST326 Final Project Test Program

Author: Haaris Malik, Jacob Levy

This code is for pulling data from the IMDB API and letting a user enter the name of any movie, 
then the code pulls all the info of that movie that has been searched by the user.
"""
import requests  


def query_movies():
    """ Asks the user for a movie name and then searches for it through the IMDB API.
    Returns:
            movie_ids (list): A list of relevant movie IDs
    """
    #Ask user for movie name
    movie_name = input('Please enter the name of the movie you would like to search: ')

    url = f"https://imdb-api.com/en/API/SearchMovie/k_59tuzoqj/{movie_name}"
    response = requests.request("GET", url)
    #Best to parse it as a json, since then we can treat it like a dictionary.
    movie_ids = []

    #Creating a list of movie IDs 
    for movie_entry in response.json()['results']:
        movie_ids.append(movie_entry['id'])

    return movie_ids

def choose_movie(movie_ids):
    """ This asks the user to pick from 5 of the movies that are outputted after searching the title by pressing either 1, 2, 3, 4, or 5.
    Args:
        movie_ids (list): A list of movie_ids, corresponding to the numbers the user can select.
    Returns:
        response (requests object): The response from the API.
    """
    # Ask user to input a value from 1-5
    entered_value = input('Press a key from 1-5 to choose a result: ')
    #Converting to an int for our conditionals.
    entered_value = int(entered_value)

    # If the input is 1, then it will pick the first choice that is displayed
    if entered_value == 1:
        id = movie_ids[1]
        url = f"https://imdb-api.com/en/API/Title/k_59tuzoqj/{id}/FullCast,Ratings,Wikipedia,"
        response = requests.request("GET", url)
        print(response.json())
        return response
    # If the input is 2, then it will pick the second choice that is displayed
    elif entered_value == 2:
        id = movie_ids[2]
        url = f"https://imdb-api.com/en/API/Title/k_59tuzoqj/{id}/FullCast,Ratings,Wikipedia,"
        response = requests.request("GET", url)
        print(response.json())
        return response
    # If the input is 3, then it will pick the third choice that is displayed
    elif entered_value == 3:
        id = movie_ids[3]
        url = f"https://imdb-api.com/en/API/Title/k_59tuzoqj/{id}/FullCast,Ratings,Wikipedia,"
        response = requests.request("GET", url)
        print(response.json())
        return response
    # If the input is 4, then it will pick the fourth choice that is displayed
    elif entered_value == 4:
        id = movie_ids[4]
        url = f"https://imdb-api.com/en/API/Title/k_59tuzoqj/{id}/FullCast,Ratings,Wikipedia,"
        response = requests.request("GET", url)
        print(response.json())
        return response
    # If the input is 5, then it will pick the fith choice that is displayed
    elif entered_value == 5:
        id = movie_ids[5]
        url = f"https://imdb-api.com/en/API/Title/k_59tuzoqj/{id}/FullCast,Ratings,Wikipedia,"
        response = requests.request("GET", url)
        print(response.json())
        return response

if __name__ in "__main__":
    movie_ids = query_movies()
    choose_movie(movie_ids)
