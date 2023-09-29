import requests


def get_anime_names():
    api_url = "https://anime-facts-rest-api.herokuapp.com/api/v1"
    response = requests.get(api_url)
    return response.json()