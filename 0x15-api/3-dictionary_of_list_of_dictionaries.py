#!/usr/bin/python3
"""Export data in the JSON format"""

import json
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/todos'
    users_url = 'https://jsonplaceholder.typicode.com/users'
    try:
        todos = requests.get(url).json()
        users = requests.get(users_url).json()
    except BaseException:
        print("Error: Could not fetch data.")
        sys.exit(1)

    # Prepare data
    data = {}
    for user in users:
        user_id = user['id']
        username = user['username']
        data[user_id] = []
        for todo in todos:
            if todo['userId'] == user_id:
                data[user_id].append({
                    'username': username,
                    'task': todo['title'],
                    'completed': todo['completed']
                })

    # Write to file
    with open('todo_all_employees.json', mode='w') as f:
        json.dump(data, f)
