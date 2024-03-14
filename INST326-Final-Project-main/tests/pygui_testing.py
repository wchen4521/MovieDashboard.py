"""
Author: Shehryar Awan

INST326 IMDB Dashboard GUI Test

This is basically a proof-of-concept for making a GUI dashboard for our final project.
"""
import PySimpleGUI as sg
import requests
import os
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv('KEY')

#The ‘tt9032400’ below is the movie’s IMDB ID. You don’t need this for every API call, but it is required for when we’re looking for the movie’s reviews.
url_search = f"https://imdb-api.com/en/API/Search/{KEY}/eternals"
url_reviews = f"https://imdb-api.com/en/API/Reviews/{KEY}/tt9032400" 
url_title = f"https://imdb-api.com/en/API/Title/{KEY}/tt1375666/FullCast,Ratings,Wikipedia"

response_reviews = requests.request("GET", url_search)
response = requests.request("GET", url_reviews)

#Best to parse it as a json, since then we can treat it like a dictionary.
movie_id = (response_reviews.json()['expression'])
movie_name = (response.json()['title']) #This is just a proof of concept. In the final project it'll need to return much more.
movie_year = (response.json()['year'])
movie_type = (response.json()['type'])


sg.theme('DarkBlue') 
#Creating the layouts we will need for our GUI. 
initial_layout = [
    [sg.Col([
    [sg.Text("Welcome to the INST326 Internet Movie Database Dashboard!", font=('Times 20 bold'), background_color="Black")],
    [sg.Text("Please type in the movie you would like to know more about", font=('Times 20'), background_color="Black")],  
    [sg.Input(key='-MOVIE_NAME-', size=(100,100))],
    [sg.Submit(), sg.Cancel()]])]
]

search_layout = [
    [sg.Col([
    [sg.Text("Search", font=('Times 20 bold'), background_color="Black")],
    [sg.Text(f"Movie Results", font=('Times 20'), background_color="Black")], 
    [sg.Checkbox('Movie 1', default=False , key = "-M1-")],
    [sg.Checkbox('Movie 2', default=False , key = "-M2-")],
    [sg.Checkbox('Movie 3', default=False , key = "-M3-")],
    [sg.Checkbox('Movie 4', default=False , key = "-M4-")],
    [sg.Checkbox('Movie 5', default=False , key = "-M5-")],
    [sg.Button("Results ", size=(10,2))],
    [sg.Button("Return", size=(10,2))],
    [sg.Button("Quit  ", size=(10,2))]])]
]

results_screen_layout = [
    [sg.Col([
    [sg.Text("Search", font=('Times 20 bold'), background_color="Black")],
    [sg.Text(f"What would you like to know about {movie_name}", font=('Times 20'), background_color="Black")],  
    [sg.Checkbox('Release Year', default=False , key = "-IN2-")],    
    [sg.Checkbox('Age Rating', default=False , key = "-IN3-")],    
    [sg.Checkbox('Runtime', default=False , key = "-IN4-")],    
    [sg.Checkbox('IMDB Score', default=False , key = "-IN5-")],   
    [sg.Checkbox('Plot Synopsis', default=False , key = "-IN6-")],   
    [sg.Checkbox('Cast', default=False , key = "-IN7-")],       [sg.Checkbox('Box Office Gross', default=False , key = "-IN8-")],    
    [sg.Checkbox('Genres', default=False , key = "-IN9-")],   
    [sg.Checkbox('Similar Movies', default=False , key = "-IN10-")],   
    [sg.Button("Results", size=(10,2))],
    [sg.Button("Return  ", size=(10,2))],
    [sg.Button("Quit", size=(10,2))]])]
]

results_screen_layout2 = [
    [sg.Col([
    [sg.Text("Search Results", font=('Times 20 bold'), background_color="Black")],
    [sg.Text(f"Results of {movie_name}", font=('Times 20'), background_color="Black", visible= False, key = "-RESULTS-")],
    [sg.Text(f"Year: {movie_year}", font=('Times 20'), background_color="Black", visible= False, key = "-YEAR-")],
    [sg.Text(f"Type: {movie_type}", font=('Times 20'), background_color="Black", visible= False, key = "-AGE-")],
    [sg.Text(f"Type: {movie_type}", font=('Times 20'), background_color="Black", visible= False, key = "-RUNTIME-")],
    [sg.Text(f"Type: {movie_type}", font=('Times 20'), background_color="Black", visible= False, key = "-SCORE-")],  
    [sg.Text(f"Type: {movie_type}", font=('Times 20'), background_color="Black", visible= False, key = "-PLOT-")],
    [sg.Text(f"Type: {movie_type}", font=('Times 20'), background_color="Black", visible= False, key = "-CAST-")],
    [sg.Text(f"Type: {movie_type}", font=('Times 20'), background_color="Black", visible= False, key = "-MONEY-")],
    [sg.Text(f"Type: {movie_type}", font=('Times 20'), background_color="Black", visible= False, key = "-GENRE-")],
    [sg.Text(f"Type: {movie_type}", font=('Times 20'), background_color="Black", visible= False, key = "-SIM-")],
    [sg.Button("Return ", size=(10,2))],
    [sg.Button("Quit ", size=(10,2))]])]
]

#The overall_layout is comprised of all the above layouts. By doing this, we can switch between the layouts and keep it to one screen.
overall_layout = [[sg.Column(initial_layout, key='-HOME_SCREEN-'), sg.Column(search_layout, visible=False, key='-SEARCH_SCREEN-'), 
    sg.Column(results_screen_layout, visible=False, key='-RESULTS_SCREEN-'), 
    sg.Column(results_screen_layout2, visible=False, key='-RESULTS_SCREEN2-')]]

# Creating the window
window = sg.Window("INST326 IMDB Dashboard", layout = overall_layout, margins = (300, 300))

# Creating an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Cancel" or event == sg.WIN_CLOSED:
        print('window closed')
        break
    
    #This conditional changes the window to a search screen of the various movies the user may pick from their searched title.
    if event == 'Submit':
        window['-HOME_SCREEN-'].update(visible=False)
        window['-SEARCH_SCREEN-'].update(visible=True)
        window['-RESULTS_SCREEN-'].update(visible=False)
        window['-RESULTS_SCREEN2-'].update(visible=False)
        
    #This will bring the user back to the home screen.
    if event == 'Return':
        window['-HOME_SCREEN-'].update(visible=True)
        window['-RESULTS_SCREEN-'].update(visible=False)       
        window['-RESULTS_SCREEN2-'].update(visible=False)
        
    if event == 'Return ':
        window['-HOME_SCREEN-'].update(visible=True)
        window['-RESULTS_SCREEN-'].update(visible=False)    
        window['-RESULTS_SCREEN2-'].update(visible=False)
        
    if event == 'Return  ':
        window['-HOME_SCREEN-'].update(visible=True)
        window['-RESULTS_SCREEN-'].update(visible=False)
        window['-RESULTS_SCREEN2-'].update(visible=False)

    
    #The following blocks of -M#- conditionals represent the result screen for one of the five movie options given.    
    if values["-M1-"] == True and event == 'Results ':
        window['-HOME_SCREEN-'].update(visible=False)
        window['-SEARCH_SCREEN-'].update(visible=False)
        window['-RESULTS_SCREEN-'].update(visible=True)        
        window['-RESULTS_SCREEN2-'].update(visible=False)
        
    if values["-M2-"] == True and event == 'Results ':
        window['-HOME_SCREEN-'].update(visible=False)        
        window['-SEARCH_SCREEN-'].update(visible=False)
        window['-RESULTS_SCREEN-'].update(visible=True)       
        window['-RESULTS_SCREEN2-'].update(visible=False)
        
    if values["-M3-"] == True and event == 'Results ':
        window['-HOME_SCREEN-'].update(visible=False)  
        window['-SEARCH_SCREEN-'].update(visible=False)
        window['-RESULTS_SCREEN-'].update(visible=True)   
        window['-RESULTS_SCREEN2-'].update(visible=False)
        
    if values["-M4-"] == True and event == 'Results ':
        window['-HOME_SCREEN-'].update(visible=False)
        window['-SEARCH_SCREEN-'].update(visible=False)
        window['-RESULTS_SCREEN-'].update(visible=True)
        window['-RESULTS_SCREEN2-'].update(visible=False)
        
    if values["-M5-"] == True and event == 'Results ':
        window['-HOME_SCREEN-'].update(visible=False)
        window['-SEARCH_SCREEN-'].update(visible=False)
        window['-RESULTS_SCREEN-'].update(visible=True)
        window['-RESULTS_SCREEN2-'].update(visible=False) 

#The following blocks of -IN#- conditionals represent the various pieces of information the user can get.
    #In this block, -IN2-, we make visible the year the movie was out.       
    if values["-IN2-"] == True and event == 'Results':     
        window['-HOME_SCREEN-'].update(visible=False)
        window['-RESULTS_SCREEN-'].update(visible=False)       
        window['-RESULTS_SCREEN2-'].update(visible=True)    
        window['-YEAR-'].update(visible=True)
        
        
    if values["-IN3-"] == True and event == 'Results':
        window['-HOME_SCREEN-'].update(visible=False)
        window['-RESULTS_SCREEN-'].update(visible=False)
        window['-RESULTS_SCREEN2-'].update(visible=True)
        window['-AGE-'].update(visible=True)
    
    if values["-IN4-"] == True and event == 'Results':
        window['-HOME_SCREEN-'].update(visible=False)
        window['-RESULTS_SCREEN-'].update(visible=False)
        window['-RESULTS_SCREEN2-'].update(visible=True)
        window['-RUNTIME-'].update(visible=True)
        
    if values["-IN5-"] == True and event == 'Results':
        window['-HOME_SCREEN-'].update(visible=False)
        window['-RESULTS_SCREEN-'].update(visible=False)
        window['-RESULTS_SCREEN2-'].update(visible=True)
        window['-SCORE-'].update(visible=True)
        
    if values["-IN6-"] == True and event == 'Results':
        window['-HOME_SCREEN-'].update(visible=False)
        window['-RESULTS_SCREEN-'].update(visible=False)
        window['-RESULTS_SCREEN2-'].update(visible=True)
        window['-PLOT-'].update(visible=True)
        
    if values["-IN7-"] == True and event == 'Results':
        window['-HOME_SCREEN-'].update(visible=False)
        window['-RESULTS_SCREEN-'].update(visible=False)
        window['-RESULTS_SCREEN2-'].update(visible=True)
        window['-CAST-'].update(visible=True)
        
    if values["-IN8-"] == True and event == 'Results':
        window['-HOME_SCREEN-'].update(visible=False)
        window['-RESULTS_SCREEN-'].update(visible=False)
        window['-RESULTS_SCREEN2-'].update(visible=True)
        window['-MONEY-'].update(visible=True)
        
    if values["-IN9-"] == True and event == 'Results':
        window['-HOME_SCREEN-'].update(visible=False)
        window['-RESULTS_SCREEN-'].update(visible=False)
        window['-RESULTS_SCREEN2-'].update(visible=True)
        window['-GENRE-'].update(visible=True)
        
    if values["-IN10-"] == True and event == 'Results':
        window['-HOME_SCREEN-'].update(visible=False)
        window['-RESULTS_SCREEN-'].update(visible=False)      
        window['-RESULTS_SCREEN2-'].update(visible=True)       
        window['-SIM-'].update(visible=True)
        
    #In case the user presses Quit, this will exit the program.     
    if event == 'Quit' or event == sg.WIN_CLOSED:
        break
    
    if event == 'Quit ' or event == sg.WIN_CLOSED:
        break
    
    if event == 'Quit  ' or event == sg.WIN_CLOSED:
        break
        
window.close()