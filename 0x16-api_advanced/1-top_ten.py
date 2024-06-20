#!/usr/bin/python3
"""1. Top Ten"""


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    the_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    client_agent = {'User-agent': 'haythm ubuntu 20.2'}
    parameters = {'limit': 10}
    res = requests.get(the_url, headers=client_agent, params=parameters,
                       allow_redirects=False)

    if res.status_code == 404:
        print("None")
        return

    try:
        result = res.json().get('data')
        [print(child.get('data').get('title'))
         for child in result.get('children')]

    except Exception:
        return 0
