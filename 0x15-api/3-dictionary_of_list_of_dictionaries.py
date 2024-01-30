#!/usr/bin/python3
""" a Python script that, using this REST API"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    employee_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    obj_dict = {}
    employee_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for employee_id in employee_ids:
        response = requests.get(employee_url, params={"id": employee_id})
        employee_res = response.json()
        employee_name = employee_res[0].get('name')
        username = employee_res[0].get('username')

        response = requests.get(todos_url, params={"userId": employee_id})
        employee_todos = response.json()
        TOTAL_NUMBER_OF_TASKS = len(employee_todos)
        NUMBER_OF_DONE_TASKS = 0
        COMPLETED_TASKS = []
        obj_list = []

        for i in employee_todos:
            if i.get("completed"):
                NUMBER_OF_DONE_TASKS += 1
                COMPLETED_TASKS.append(i)
            title = f'{i.get("title")}'
            status = i.get("completed")
            obj = {"username": username, "task": title, "completed": status}
            obj_list.append(obj)

        print(f"Employee {employee_name} is done with "
              f"tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

        for i in COMPLETED_TASKS:
            print(f"\t {i.get('title')}")

        obj_dict[employee_id] = obj_list

    # convert to json
    filename = 'todo_all_employees.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(obj_dict, f)
