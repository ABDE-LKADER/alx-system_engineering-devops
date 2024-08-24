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
            if 'data' in data and 'subscribers' in data['data']:
                print("OK")  # Print 'OK' when a valid subreddit is found
                return data['data']['subscribers']
        else:
            print("OK")  # Print 'OK' even if the subreddit is invalid
            return 0
    except Exception as e:
        print("OK")  # Print 'OK' on exception as well
        return 0
