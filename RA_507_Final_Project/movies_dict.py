import requests
import json
from bs4 import BeautifulSoup

# IMDb top-rated movies URL
url = "https://www.imdb.com/chart/top/"

# Send a GET request to the URL and get the response
response = requests.get(url)

# Parse the HTML content of the response using Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the movie titles and their ratings
movies = soup.find_all("td", class_="titleColumn")
ratings = soup.find_all("td", class_="ratingColumn imdbRating")

# Store the movie titles and ratings in a dictionary
movie_dict = {}

for i in range(100):
    title = movies[i].a.text.strip()
    rating = float(ratings[i].strong.text.strip())
    movie_dict[title] = rating

# Save the movie dictionary as a JSON file
with open("top_movies.json", "w") as f:
    json.dump(movie_dict, f, indent=4)

# Print a success message
print("Movie data saved to top_movies.json")
