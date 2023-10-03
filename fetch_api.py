import requests
import os
MAL_CLIENT_ID = os.getenv("MAL_CLIENT_ID") 
MAL_CLIENT_SECRET = os.getenv("MAL_CLIENT_SECRET") 
from requests.auth import HTTPBasicAuth

def get_anime_names():
    url = "https://api.myanimelist.net/v2"
    headers = {'Accept': 'application/json'}
    auth = HTTPBasicAuth(MAL_CLIENT_ID, MAL_CLIENT_SECRET)
    # files = {'file': open('filename', 'rb')}
    files = {'file': open('filename','rb')}

    req = requests.get(url, headers=headers, auth=auth, files=files)

if __name__ == "__main__":
    get_anime_names()