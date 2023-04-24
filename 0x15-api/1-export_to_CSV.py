#!/usr/bin/python3
"""
Python script that, using the REST API (https://jsonplaceholder.typicode.com/), for a given employee ID,
returns information about his/her TODO list progress and export data in the CSV format.
"""

import csv
import requests
from sys import argv


def get_todo_list(employee_id):
    """Returns information about the employee's TODO list progress"""
    url = 'https://jsonplaceholder.typicode.com'
    employee = requests.get('{}/users/{}'.format(url, employee_id)).json()
    tasks = requests.get('{}/todos?userId={}'.format(url, employee_id)).json()
    return employee, tasks


def export_to_csv(employee_id):
    """Exports the employee's TODO list progress to a CSV file"""
    employee, tasks = get_todo_list(employee_id)

    with open('{}.csv'.format(employee_id), mode='w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in tasks:
            writer.writerow([employee_id,
                             employee.get('username'),
                             task.get('completed'),
                             task.get('title')])


if __name__ == '__main__':
    employee_id = int(argv[1])
    export_to_csv(employee_id)
