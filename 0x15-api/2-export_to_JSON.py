#!/usr/bin/python3
"""
Extend your Python script to export data in the JSON format.
"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(user_id)).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(user_id)).json()

    with open('{}.json'.format(user_id), mode='w') as file:
        data = {}
        data[user_id] = []
        for task in todo:
            task_dict = {}
            task_dict['task'] = task.get('title')
            task_dict['completed'] = task.get('completed')
            task_dict['username'] = user.get('username')
            data[user_id].append(task_dict)
        json.dump(data, file)
