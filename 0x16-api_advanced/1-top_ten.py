#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, print None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 10}

    try:
        req = requests.get(url, headers=headers, params=params, allow_redirects=False)
        # Check if response is valid JSON
        if req.status_code == 200:
            data = req.json()
            posts = data.get("data", {}).get("children", [])
            for post in posts:
                print(post.get("data", {}).get("title"))
        else:
            # If status code is not 200, handle errors
            print(None)
    except ValueError:
        # If JSON decoding fails
        print(None)
    except requests.exceptions.RequestException as e:
        # Handle any request errors
        print(None)
