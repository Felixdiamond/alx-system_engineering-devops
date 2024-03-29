#!/usr/bin/python3

"""
    Queries the Reddit API and prints the titles of the first 10
    hot posts listed for a given subreddit.

    Args:
      subreddit: The name of the subreddit to query.

    Returns:
      None.
    """

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Ayanokoji/2.1"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
