#!/usr/bin/python3
"""
This module provides functions to read and write CSV files.

Functions:
    read_csv: Read data from a CSV file.
    write_csv: Write data to a CSV file.
"""
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
