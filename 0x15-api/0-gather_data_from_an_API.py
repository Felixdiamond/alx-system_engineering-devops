#!/usr/bin/python3

"""
This script retrieves information about an employee's TODO list progress
from a REST API and displays it in a specific format.

Usage: ./0-gather_data_from_an_API.py [employee_id]
"""

import requests
import sys

def get_employee_todo_list(employee_id):
    """Retrieves the employee's TODO list from the API"""

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)
    response = requests.get(url)

    if response.status_code != 200:
        print('Error: Employee not found')
        sys.exit()

    todo_list = response.json()

    return todo_list

def display_employee_todo_list(employee_id):
    """Displays the employee's TODO list in a specific format"""

    todo_list = get_employee_todo_list(employee_id)

    # Count the number of completed tasks
    num_completed = 0
    for task in todo_list:
        if task['completed']:
            num_completed += 1

    # Display the employee's name and progress
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    response = requests.get(url)
    employee_name = response.json()['name']
    total_tasks = len(todo_list)
    print("Employee {} is done with tasks({}/{}):".format(employee_name, num_completed, total_tasks))

    # Display the titles of completed tasks
    for task in todo_list:
        if task['completed']:
            print("\t {}".format(task['title']))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: ./file.py [employee_id]')
        sys.exit()

    employee_id = sys.argv[1]
    display_employee_todo_list(employee_id)
