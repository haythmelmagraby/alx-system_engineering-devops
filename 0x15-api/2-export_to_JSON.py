#!/usr/bin/python3
""" Export to JSON """
import json
from sys import argv
import requests

if __name__ == "__main__":
    eid = argv[1]
    user = "https://jsonplaceholder.typicode.com/users"
    url = user + "/" + eid

    res = requests.get(url)
    user_name = res.json().get("username")

    tds = url + "/todos"
    res = requests.get(todoUrl)
    task = res.json()

    dicte = {eid: []}
    for the_task in task:
        dic[eid].append(
            {
                "task": the_task.get("title"),
                "completed": the_task.get("completed"),
                "username": user_name,
            }
        )

    with open("{}.json".format(eid), "w") as f:
        json.dump(dicte, f)
