import requests
import random

def get_random_joke():
    response = requests.get('https://v2.jokeapi.dev/joke/Any')
    if response.status_code == 200:
        joke_data = response.json()
        if joke_data['type'] == 'single':  
            return joke_data['joke']
        else:
            return f"{joke_data['setup']} - {joke_data['delivery']}"
    else:
        return "Failed to fetch joke"

if __name__ == '__main__':
    print(get_random_joke())