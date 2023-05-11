#!/usr/bin/python3

"""
    Queries the Reddit API and returns a list containing the titles of all hot 
    articles for a given subreddit.

    Args:
      subreddit: The name of the subreddit to query.
      hot_list: A list to store the titles of the hot articles.

    Returns:
      A list containing the titles of the hot articles.
    """

import requests


def recurse(subreddit, hot_list=[]):

    # Check if the subreddit is valid.
    if not subreddit:
        print("Please provide a valid subreddit name.")
        return

    # Make a request to the Reddit API.
    response = requests.get(
        "https://api.reddit.com/r/{}/hot.json?limit=100".format(subreddit),
        allow_redirects=False,
        headers={
            "User-Agent": "Ayanokoji/2.1"})

    # Check if the request was successful.
    if response.status_code != 200:
        print("Error: {} {}".format(response.status_code, response.reason))
        return

    # Parse the response data.
    data = response.json()

    # Check if the subreddit exists.
    if "subreddit" not in data:
        print("Subreddit {} does not exist.".format(subreddit))
        return

    # Iterate over the hot articles.
    for post in data["data"]["children"]:
        hot_list.append(post["data"]["title"])

    # Check if there are more pages of results.
    if "after" in data["data"]["after"]:
        return recurse(subreddit, hot_list, data["data"]["after"])

    # Return the list of hot articles.
    return hot_list
