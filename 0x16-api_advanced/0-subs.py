#!/usr/bin/python3

"""
number_of_subscribers(subreddit)

Returns the number of subscribers for a given subreddit.

Args:
  subreddit (str): The name of the subreddit.

Returns:
  int: The number of subscribers.

Raises:
  ValueError: If the subreddit is not valid.
"""

from fake_useragent import UserAgent
import requests

def number_of_subscribers(subreddit):
    response = requests.get('https://api.reddit.com/r/{}/about.json'.format(subreddit), allow_redirects=False, headers={
                             "User-Agent": ua.random})
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
