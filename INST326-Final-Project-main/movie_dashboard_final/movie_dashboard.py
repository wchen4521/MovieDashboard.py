"""
INST326 Final Project: Movie Dashboard 

Authors: Jacob Levy, Haaris Malik, Shehryar Awan, Chen Wang
"""
import os
from dotenv import load_dotenv
import requests
import PySimpleGUI as sg
from pulling_data import movie_options, chosen_movie
from parse_data import parse_response

load_dotenv()
KEY = os.getenv('KEY')

sg.theme('DarkBlue') 
#Creating the layout we will need for our GUI. 
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
    [sg.Checkbox(f'Movie Name 1', default=False , key = "-M1-")],
    [sg.Checkbox(f'Movie Name 2', default=False , key = "-M2-")],
    [sg.Checkbox(f'Movie Name 3', default=False , key = "-M3-")],
    [sg.Checkbox(f'Movie Name 4', default=False , key = "-M4-")],
    [sg.Checkbox(f'Movie Name 5', default=False , key = "-M5-")],
    [sg.Button("Results ", size=(10,2))],
    [sg.Button("Return", size=(10,2))],
    [sg.Button("Quit  ", size=(10,2))]])]
]


results_screen_layout = [
    [sg.Col([
    [sg.Text("Search", font=('Times 20 bold'), background_color="Black")],
    [sg.Text(f"What would you like to know about", font=('Times 20'), background_color="Black", key = '-RESULT_NAME-')], 
    [sg.Checkbox('Release Year', default=False , key = "-IN2-")], 
    [sg.Checkbox('Age Rating', default=False , key = "-IN3-")],
    [sg.Checkbox('Runtime', default=False , key = "-IN4-")],
    [sg.Checkbox('IMDB Score', default=False , key = "-IN5-")],
    [sg.Checkbox('Plot Synopsis', default=False , key = "-IN6-")],
    [sg.Checkbox('Cast', default=False , key = "-IN7-")],
    [sg.Checkbox('Box Office Gross', default=False , key = "-IN8-")],
    [sg.Checkbox('Genres', default=False , key = "-IN9-")],
    [sg.Checkbox('Similar Movies', default=False , key = "-IN10-")],
    [sg.Button("Results", size=(10,2))],
    [sg.Button("Return  ", size=(10,2))],
    [sg.Button("Quit", size=(10,2))]])]
]


results_screen_layout2 = [
    [sg.Col([
    [sg.Text("Search Results", font=('Times 20 bold'), background_color="Black")],
    [sg.Text(f"Results of ", font=('Times 20'), background_color="Black", visible= False, key = "-RESULTS-")],
    [sg.Text(f"Year: ", font=('Times 20'), background_color="Black", visible= False, key = "-YEAR-")],
    [sg.Text(f"Age Rating:", font=('Times 20'), background_color="Black", visible= False, key = "-AGE-")],
    [sg.Text(f"Runtime: ", font=('Times 20'), background_color="Black", visible= False, key = "-RUNTIME-")],
    [sg.Text(f"IMDB Score: ", font=('Times 20'), background_color="Black", visible= False, key = "-SCORE-")],
    [sg.Text(f"Plot Synopsis:", font=('Times 20'), background_color="Black", visible= False, key = "-PLOT-")],
    [sg.Text(f"Cast: ", font=('Times 20'), background_color="Black", visible= False, key = "-CAST-")],
    [sg.Text(f"Box Office Gross:", font=('Times 20'), background_color="Black", visible= False, key = "-MONEY-")],
    [sg.Text(f"Genres: ", font=('Times 20'), background_color="Black", visible= False, key = "-GENRE-")],
    [sg.Text(f"Similar Movies:", font=('Times 20'), background_color="Black", visible= False, key = "-SIM-")],
    [sg.Button("Return ", size=(10,2))],
    [sg.Button("Quit ", size=(10,2))]])]
]

#The overall_layout is comprised of all the layouts. By doing this, we can switch between the layouts and keep it to one screen.
overall_layout = [[sg.Column(initial_layout, key='-HOME_SCREEN-'), 
    sg.Column(search_layout, visible=False, key='-SEARCH_SCREEN-'), 
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
        movie_name = values['-MOVIE_NAME-']
        #Calling movie_options to search the API by movie name, which will return a list of movie names and IDs
        result_ids, result_names = movie_options(KEY, movie_name)
        #Dynamically updating the names of the movies the user can choose, based on the IMDB search results.
        window.Element('-M1-').update(text = f'{result_names[0]}')
        window.Element('-M2-').update(text = f'{result_names[1]}')
        window.Element('-M3-').update(text = f'{result_names[2]}')
        window.Element('-M4-').update(text = f'{result_names[3]}')
        window.Element('-M5-').update(text = f'{result_names[4]}')

        #Updating the layout to display the search screen, now with the updated movie titles.
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
        response = chosen_movie(KEY, result_ids[0])
        movie = parse_response(response) 
        #This block dynamically updates the names and values for the various pieces of information we can give the user.
        window.Element('-RESULT_NAME-').update(value = f'What would you like to know about {movie.fullTitle}')
        window.Element('-YEAR-').update(value = f'Year: {movie.year}')
        window.Element('-AGE-').update(value = f'Age Rating: {movie.age_rating}')
        window.Element('-RUNTIME-').update(value = f'Runtime: {movie.runtime}')
        window.Element('-SCORE-').update(value = f'IMDB Score: {movie.imdb_rating}')
        window.Element('-PLOT-').update(value = f'Plot Synopsis: {movie.plot}')
        window.Element('-CAST-').update(value = f'Cast: {movie.casting}')
        window.Element('-MONEY-').update(value = f'Box Office Gross: {movie.money}')
        window.Element('-GENRE-').update(value = f'Genres: {movie.genres}')
        window.Element('-SIM-').update(value = f'Similar Movies: {movie.similar_movies}')
        
        #Updating the results screen to show the chosen movie.
        window['-HOME_SCREEN-'].update(visible=False)
        window['-SEARCH_SCREEN-'].update(visible=False)
        window['-RESULTS_SCREEN-'].update(visible=True)     
        window['-RESULTS_SCREEN2-'].update(visible=False)
        
    if values["-M2-"] == True and event == 'Results ':
        response = chosen_movie(KEY, result_ids[1])
        movie = parse_response(response) 
        #This block dynamically updates the names and values for the various pieces of information we can give the user.
        window.Element('-RESULT_NAME-').update(value = f'Results of {movie.fullTitle}')
        window.Element('-YEAR-').update(value = f'Year: {movie.year}')
        window.Element('-AGE-').update(value = f'Age Rating: {movie.age_rating}')
        window.Element('-RUNTIME-').update(value = f'Runtime: {movie.runtime}')
        window.Element('-SCORE-').update(value = f'IMDB Score: {movie.imdb_rating}')
        window.Element('-PLOT-').update(value = f'Plot Synopsis: {movie.plot}')
        window.Element('-CAST-').update(value = f'Cast: {movie.casting}')
        window.Element('-MONEY-').update(value = f'Box Office Gross: {movie.money}')
        window.Element('-GENRE-').update(value = f'Genres: {movie.genres}')
        window.Element('-SIM-').update(value = f'Similar Movies: {movie.similar_movies}')
        
        window['-HOME_SCREEN-'].update(visible=False)
        window['-SEARCH_SCREEN-'].update(visible=False)
        window['-RESULTS_SCREEN-'].update(visible=True)
        window['-RESULTS_SCREEN2-'].update(visible=False)
        
    if values["-M3-"] == True and event == 'Results ':
        response = chosen_movie(KEY, result_ids[2])
        movie = parse_response(response) 
        #This block dynamically updates the names and values for the various pieces of information we can give the user.
        window.Element('-RESULT_NAME-').update(value = f'Results of {movie.fullTitle}')
        window.Element('-YEAR-').update(value = f'Year: {movie.year}')
        window.Element('-AGE-').update(value = f'Age Rating: {movie.age_rating}')
        window.Element('-RUNTIME-').update(value = f'Runtime: {movie.runtime}')
        window.Element('-SCORE-').update(value = f'IMDB Score: {movie.imdb_rating}')
        window.Element('-PLOT-').update(value = f'Plot Synopsis: {movie.plot}')
        window.Element('-CAST-').update(value = f'Cast: {movie.casting}')
        window.Element('-MONEY-').update(value = f'Box Office Gross: {movie.money}')
        window.Element('-GENRE-').update(value = f'Genres: {movie.genres}')
        window.Element('-SIM-').update(value = f'Similar Movies: {movie.similar_movies}')

        window['-HOME_SCREEN-'].update(visible=False)
        window['-SEARCH_SCREEN-'].update(visible=False)
        window['-RESULTS_SCREEN-'].update(visible=True)
        window['-RESULTS_SCREEN2-'].update(visible=False)
        
    if values["-M4-"] == True and event == 'Results ':
        response = chosen_movie(KEY, result_ids[3])
        movie = parse_response(response) 
        #This block dynamically updates the names and values for the various pieces of information we can give the user.
        window.Element('-RESULT_NAME-').update(value = f'Results of {movie.fullTitle}')
        window.Element('-YEAR-').update(value = f'Year: {movie.year}')
        window.Element('-AGE-').update(value = f'Age Rating: {movie.age_rating}')
        window.Element('-RUNTIME-').update(value = f'Runtime: {movie.runtime}')
        window.Element('-SCORE-').update(value = f'IMDB Score: {movie.imdb_rating}')
        window.Element('-PLOT-').update(value = f'Plot Synopsis: {movie.plot}')
        window.Element('-CAST-').update(value = f'Cast: {movie.casting}')
        window.Element('-MONEY-').update(value = f'Box Office Gross: {movie.money}')
        window.Element('-GENRE-').update(value = f'Genres: {movie.genres}')
        window.Element('-SIM-').update(value = f'Similar Movies: {movie.similar_movies}')
        
        window['-HOME_SCREEN-'].update(visible=False)
        window['-SEARCH_SCREEN-'].update(visible=False)
        window['-RESULTS_SCREEN-'].update(visible=True)
        window['-RESULTS_SCREEN2-'].update(visible=False)
        
    if values["-M5-"] == True and event == 'Results ':
        response = chosen_movie(KEY, result_ids[4])
        movie = parse_response(response) 
        #This block dynamically updates the names and values for the various pieces of information we can give the user.
        window.Element('-RESULT_NAME-').update(value = f'Results of {movie.fullTitle}')
        window.Element('-YEAR-').update(value = f'Year: {movie.year}')
        window.Element('-AGE-').update(value = f'Age Rating: {movie.age_rating}')
        window.Element('-RUNTIME-').update(value = f'Runtime: {movie.runtime}')
        window.Element('-SCORE-').update(value = f'IMDB Score: {movie.imdb_rating}')
        window.Element('-PLOT-').update(value = f'Plot Synopsis: {movie.plot}')
        window.Element('-CAST-').update(value = f'Cast: {movie.casting}')
        window.Element('-MONEY-').update(value = f'Box Office Gross: {movie.money}')
        window.Element('-GENRE-').update(value = f'Genres: {movie.genres}')
        window.Element('-SIM-').update(value = f'Similar Movies: {movie.similar_movies}')
        
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