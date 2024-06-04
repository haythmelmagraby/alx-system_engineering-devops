#!/usr/bin/python3
""" Dictionary of list of dictionaries """
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"

    res = requests.get(url)
    users = res.json()

    dicte = {}
    for user in users:
        user_Id = user.get("id")
        user_name = user.get("username")
        url = "https://jsonplaceholder.typicode.com/users/{}".format(user_Id)
        url = url + "/todos/"
        res = requests.get(url)
        task = res.json()
        dicte[user_Id] = []

        for the_task in task:
            dicte[user_Id].append(
                {
                    "task": the_task.get("title"),
                    "completed": the_task.get("completed"),
                    "username": user_name,
                }
            )

    with open("todo_all_employees.json", "w") as f:
        json.dump(dicte, f)
