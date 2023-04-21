from flask import Flask, render_template, request
import requests
import json
import time
from sortedcontainers import SortedDict

app = Flask(__name__, template_folder='templates')

# TMDb API key
api_key = "ceb4fa12c500ed8888d00bc500a6ec1b"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results')
def results():
    # Get the user input from the form
    movie_title = request.args.get('movie_title')

    # Check if the movie details are already in the cache
    with open("movie_details_cache.json", "r") as f:
        movie_details = json.load(f)
    if movie_title in movie_details:
        details = movie_details[movie_title]
    else:
        # Send a GET request to the TMDb API to search for the movie
        search_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_title}"
        response = requests.get(search_url)

        # Get the movie ID from the search results
        results = response.json()["results"]
        if len(results) == 0:
            return "Movie not found."
        movie_id = results[0]["id"]

        # Send a GET request to the TMDb API to retrieve the movie details
        details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
        response = requests.get(details_url)

        # Parse the JSON response and extract the relevant movie details
        data = response.json()
        rating = data["vote_average"]
        genres = [genre["name"] for genre in data["genres"]]

        # Store the movie details in the dictionary and the cache
        details = {"rating": rating, "genres": genres}
        movie_details[movie_title] = details
        with open("movie_details_cache.json", "w") as f:
            json.dump(movie_details, f, indent=4)

    # Render the template with the movie details
    return render_template('results.html', movie_title=movie_title, rating=details["rating"], genres=details["genres"])

if __name__ == "__main__":
    app.run(debug=True)
