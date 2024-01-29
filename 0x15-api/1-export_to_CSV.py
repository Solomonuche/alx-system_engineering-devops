#!/usr/bin/python3
""" a Python script that, using this REST API"""
from csv import writer, QUOTE_ALL
import requests
from sys import argv


if __name__ == "__main__":
    employee_url = 'https://jsonplaceholder.typicode.com/users'
    employee_todos = 'https://jsonplaceholder.typicode.com/todos'
    if argv[1]:
        employee_id = argv[1]

    response = requests.get(employee_url, params={"id": employee_id})
    employee_res = response.json()
    employee_name = employee_res[0].get('name')
    username = employee_res[0].get('username')

    response = requests.get(employee_todos, params={"userId": employee_id})
    employee_todos = response.json()
    TOTAL_NUMBER_OF_TASKS = len(employee_todos)
    NUMBER_OF_DONE_TASKS = 0
    COMPLETED_TASKS = []
    csv_file = []

    for i in employee_todos:
        if i.get("completed"):
            NUMBER_OF_DONE_TASKS += 1
            COMPLETED_TASKS.append(i)
        title = f'{i.get("title")}'
        obj = [employee_id, username, f'{i.get("completed")}', title]
        csv_file.append(obj)

    print(f"Employee {employee_name} is done with tasks({NUMBER_OF_DONE_TASKS}"
          f"/{TOTAL_NUMBER_OF_TASKS}):")

    for i in COMPLETED_TASKS:
        print(f"\t {i.get('title')}")

    # exporting to csv
    filename = f'{employee_id}.csv'
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        write = writer(f, quoting=QUOTE_ALL)

        write.writerows(csv_file)
