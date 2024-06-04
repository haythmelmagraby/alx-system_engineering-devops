#!/usr/bin/python3
""" Export to CSV """
from sys import argv
import requests

if __name__ == "__main__":
    eid = argv[1]
    user = "https://jsonplaceholder.typicode.com/users"
    url = user + "/" + eid

    res = requests.get(url)
    user_name = res.json().get("username")

    tds = url + "/todos"
    res = requests.get(tds)
    task = res.json()

    with open("{}.csv".format(eid), "w") as f:
        for the_task in task:
            f.write(
                '"{}","{}","{}","{}"\n'.format(
                    eid, user_name, the_task.get("completed"),
                    the_task.get("title")
                )
            )
