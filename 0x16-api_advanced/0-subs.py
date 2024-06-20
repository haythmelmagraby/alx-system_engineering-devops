"""0. How many subs?"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    the_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    client_agent = {'User-agent': 'haythm ubuntu 20.2'}
    res = requests.get(the_url, headers=client_agent, allow_redirects=False)
    try:
        return res.json().get('data').get('subscribers')
    except Exception:
        return 0
