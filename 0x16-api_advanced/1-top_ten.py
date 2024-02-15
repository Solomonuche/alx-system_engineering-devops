#!/usr/bin/python3
"""a function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """a function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit."""

    if subreddit:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
        try:
            res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            # raise an error is request fails
            res.raise_for_status()

            res = res.json()
            if 'data' in res and 'children' in res['data']:
                if len(res['data']['children']) > 0:
                    for post in res['data']['children']:
                        print(post['data']['title'])
                else:
                    print('None')
        except requests.exceptions.RequestException as e:
            print('None')
    else:
        print('None')
