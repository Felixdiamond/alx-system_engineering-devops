#!/usr/bin/python3
"""
Using a REST API, for a given employee ID, returns information about
his/her TODO list progress.
"""

import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    api_url = "https://jsonplaceholder.typicode.com/"
    user_url = "{}users/{}".format(api_url, user_id)
    todo_url = "{}todos?userId={}".format(api_url, user_id)

    user_req = requests.get(user_url)
    user_json = user_req.json()

    todo_req = requests.get(todo_url)
    todo_json = todo_req.json()

    completed_tasks = [task for task in todo_json if task["completed"]]
    total_tasks = len(todo_json)
    done_tasks = len(completed_tasks)
    user_name = user_json.get("name")

    print("Employee {} is done with tasks({}/{}):".format(user_name,
          done_tasks, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
