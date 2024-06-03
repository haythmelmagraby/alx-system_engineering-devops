#!/usr/bin/python3
""" Gather data from an API """
mport requests
from sys import argv


if __name__ == '__main__':
    eid = argv[1]
    user = "https://jsonplaceholder.typicode.com/users"
    url = user + "/" + eid

    response = requests.get(url)
    EMPLOYEE_NAME = response.json().get('name')

    tds = url + "/todos"
    res = requests.get(tds)
    task = res.json()
    allTasks = len(task)

    NUMBER_OF_DONE_TASKS = 0
    tasks_List = []

    for the_task in task:
        if the_task.get('completed'):
            tasks_List.append(the_task)
            NUMBER_OF_DONE_TASKS += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, allTasks))

    for the_task in tasks_List:
        print("\t {}".format(the_task.get('title')))
