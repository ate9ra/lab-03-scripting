import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'


def reterieve_events(url):
   """Gets the events from the API and returns them as a list"""
   text = requests.get(url).text
   return json.loads(text)

def print_events(events, n=5):
    """Prints the type and repo name for the events"""
    for x in events[:n]:
        event = x['type'] + ' :: ' + x['repo']['name']
        print(event)

def main():
    """Prints the username, URL, and events"""
    print(GHUSER)
    print(url)
    event = reterieve_events(url)
    print_events(event)

if __name__ == "__main__":
    main()
