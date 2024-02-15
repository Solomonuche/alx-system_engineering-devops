#!/usr/bin/python3
"""a function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """a function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit."""

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    res = requests.get(url,
                       headers={'User-Agent': 'My-User-Agent'},
                       allow_redirects=False)

    if res.status_code >= 300:
        print('None')
    else:
        res = res.json()
        for post in res['data']['children']:
            print(post['data']['title'])
