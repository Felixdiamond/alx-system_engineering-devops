#!/usr/bin/python3
""" Export user tasks to CSV """
import csv
import requests
from sys import argv


user_id = argv[1] if argv[1:] else 1
    FILENAME = user_id + ".csv"
    url = 'https://jsonplaceholder.typicode.com/'
    user = rq.get(url + 'users/{}'.format(user_id)).json()
    tasks = rq.get(url + 'users/{}/todos'.format(user_id)).json()
    with open(FILENAME, 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        [writer.writerow([user_id, user.get('username'), task.get('completed'),
                          task.get('title')]) for task in tasks]
