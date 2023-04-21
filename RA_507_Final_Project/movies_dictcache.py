import requests
import json
import time

# TMDb API key
api_key = "ceb4fa12c500ed8888d00bc500a6ec1b"

# Load the top movie titles and ratings from the JSON file
with open("top_movies.json", "r") as f:
    top_movies = json.load(f)

# Initialize a dictionary to store the movie details
movie_details = {}

# Loop through the top movies and retrieve their details from the TMDb API
for title in top_movies.keys():
    # Check if the movie details are already in the cache
    if title in movie_details:
        continue

    # Send a GET request to the TMDb API to search for the movie
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={title}"
    response = requests.get(search_url)

    # Get the movie ID from the search results
    results = response.json()["results"]
    if len(results) == 0:
        continue
    movie_id = results[0]["id"]

    # Send a GET request to the TMDb API to retrieve the movie details
    details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    response = requests.get(details_url)

    # Parse the JSON response and extract the relevant movie details
    data = response.json()
    print(data)
    title = data["title"]
    rating = data["vote_average"]
    genres = [genre["name"] for genre in data["genres"]]
    

    # Store the movie details in the dictionary and the cache
    movie_details[title] = {"rating": rating, "genres": genres}

    # Wait for 0.1 seconds to avoid exceeding the TMDb API rate limit
    time.sleep(0.1)

    # Save the movie details in a cache file to avoid making duplicate API calls
    with open("movie_details_cache.json", "w") as f:
        json.dump(movie_details, f, indent=4)

# Print the movie details
print(movie_details)
