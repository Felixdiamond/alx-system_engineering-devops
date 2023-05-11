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


def recurse(subreddit, hot_list=[], url):

    url = 'https://www.reddit.com/r/{}/hot.json?limit=1'.format(
        subreddit)

    # Make a request to the Reddit API.
    response = requests.get(
        url,
        allow_redirects=False,
        headers={
            "User-Agent": "Ayanokoji/2.1"})

    # Check if the request was successful.
    if response.status_code != 200:
        print(None)
    else:
        data = response.json()
        if 'after' in data['data']:
            after = data['data']['after']
            url += '?after={}'.format(after)
            title = data['data']['children']['data']['title']
            recurse(subreddit, hot_list.append(title), url)

        return hot_list
