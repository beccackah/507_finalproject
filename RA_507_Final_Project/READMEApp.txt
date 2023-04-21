Movie Details App
This is a simple Flask web application that allows users to search for movie details using the TMDb API.

Prerequisites
Python 3.x
Flask
requests
sortedcontainers
You can install the required packages by running the following command:

Copy code
pip install flask requests sortedcontainers
Running the App
Clone this repository to your local machine.

Navigate to the project directory in your terminal.

Run the following command to start the Flask server:

Copy code
python app.py
Open your web browser and go to http://localhost:5000/.

Enter a movie title in the search box and click the "Search" button.

The app will display the movie's rating and genres.

Interacting with the Program
The user enters a movie title in the search box on the home page and clicks the "Search" button.
The app sends a GET request to the TMDb API to search for the movie details.
If the movie details are found in the cache, the app retrieves them from the cache. Otherwise, the app retrieves them from the TMDb API and stores them in the cache.
The app displays the movie's rating and genres on the results page.