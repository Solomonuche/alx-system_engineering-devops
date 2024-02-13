#!/usr/bin/python3
"""a function that queries the Reddit API and
returns the number of subscribers """

from sys import argv
import requests


def number_of_subscribers(subreddit):
    """ a function that queries the Reddit API and returns the
    number of subscribers (not active users, total subscribers)
    for a given subreddit """

    if subreddit:
        # search that the sebreddit exits
        url = f'https://www.reddit.com/r/{subreddit}/about.json'
        res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).json()
        if 'data' in res and 'subscribers' in res['data']:
            subscribers = res['data']['subscribers']

            return subscribers
        else:
            return 0
    else:
        return 0
