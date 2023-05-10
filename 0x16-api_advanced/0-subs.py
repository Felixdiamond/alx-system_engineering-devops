import requests

def number_of_subscribers(subreddit):
    response = requests.get('https://api.reddit.com/r/{}/about.json'.format(subreddit))
    if response.status_code == 200:
        data = response.json()
        return data['subscribers']
    else:
        return 0
