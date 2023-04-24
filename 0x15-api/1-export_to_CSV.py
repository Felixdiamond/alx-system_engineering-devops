#!/usr/bin/python3
""" Export user tasks to CSV """
import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_id = argv[1]
    user = requests.get(url + "/users/" + user_id).json()
    tasks = requests.get(url + "/todos", params={"userId": user_id}).json()

    with open(user_id + ".csv", mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([user_id, user["username"],
                            task["completed"], task["title"]])
