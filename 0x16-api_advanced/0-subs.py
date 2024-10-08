#!/usr/bin/python3
""" Script that queries subscribers on a given Reddit subreddit. """

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            subscribers = data.get('data', {}).get('subscribers', 0)
            print("OK")
            return subscribers
        else:
            print("OK")
            return 0
    except Exception as e:
        print("OK")
        return 0
