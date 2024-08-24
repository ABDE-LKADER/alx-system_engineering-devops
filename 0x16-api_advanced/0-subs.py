#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""


import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'subscribers' in data['data']:
                return data['data']['subscribers']
        else:
            print("Error: Status code {}".format(response.status_code))
            return 0
    except Exception as e:
        print("Request failed: {}".format(e))
        return 0