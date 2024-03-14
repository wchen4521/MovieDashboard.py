# INST326 Final Project: Rotten Tomatoes Movie Dashboard
This repository contains the files for my INST326 Final Project. 

# Instructions for Professor Cruz & TA's.
The final version of this program can be found in the movie_dashboard_final folder. Please download all scripts.
Additionally, you will need to install the following dependencies:

[PySimpleGui](https://pysimplegui.readthedocs.io/en/latest/)

[requests](https://docs.python-requests.org/en/latest/user/install/)

[dotenv](https://pypi.org/project/python-dotenv/)

**You will also need to get the .env file, which contains the API key. You may find it on our class Discord in the project-5-movie-db channel. Put it in the same directory as the scripts.**

# Final Project Design
## Overview of the project.
I would like to create a command-line dashboard for movies. The idea is that a user can type in a movie and see detailed information about it, including but not limited to its IMDB score and listed genres. 
## Specific Goals
* A fully functional, aesthetically pleasing dashboard with a unique GUI.
* A competent integration of the IMDB API - which may be utilized multiple times throughout the program.
* The ability to query a movie and see its IMDB review score, genre, and movies like it. Additionally, the dashboard should provide optional extra information such as select metadata about the movie and a few review excerpts. 
* The entire program is well documented with comments and docstrings. 
* Sensitive information, such as API keys, are not displayed publicly. Instead, one may find them in a .env file.

## Design: API
The documentation for the IMDB API can be found here: https://imdb-api.com/

## Design: Imports
The following are imports that I should use in my program and why.
If you have something you want to add to this list, feel free to do so!

Import requests - To send the HTTP requests and get the data.

From dotenv import load_dotenv - To keep the API keys out of the code itself. Putting any API key up on Github is a bad idea.

Import PySimpleGUI as sg - The GUI I will be using to display the data.

## Design: Pulling the Data
Getting the data doesn’t take too much work. The requests library makes it as easy as this:
```
import requests
#The ‘tt9032400’ below is the movie’s IMDB ID. You don’t need this for every API call, but it is required for when you're looking for the movie’s reviews.
#So, when you're initially searching for the movie, make sure to save the ID!
url = f"https://imdb-api.com/en/API/Reviews/{KEY}/tt9032400" 
 
response = requests.request("GET", url)
#Best to parse it as a json, since then you can treat it like a dictionary.
print(response.json())
```


Design: Parsing Through the Data
If I parse it as a JSON, then you can easily look for what I want. Here’s how I would get the year it released and title:
```
print(response.json()['year'])
print(response.json()['title'])
print(response.json()['review'])
print(response.json()['imDbld'])
print(response.json()['fullTitle'])
print(response.json()['type'])
print(response.json()['rate'])
```
I will be leveraging the power of classes here in the final version by creating a Movie class with the data above as attributes. That way, I can easily access any useful data from a specific movie.

