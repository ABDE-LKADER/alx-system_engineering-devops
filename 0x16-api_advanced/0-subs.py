#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    # Make the request
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Ensure the 'data' key exists and has the 'subscribers' key
            if 'data' in data and 'subscribers' in data['data']:
                return data['data']['subscribers']
        # Return 0 if not successful or key doesn't exist
        return 0
    except requests.RequestException:
        # Return 0 if any request exception occurs
        return 0