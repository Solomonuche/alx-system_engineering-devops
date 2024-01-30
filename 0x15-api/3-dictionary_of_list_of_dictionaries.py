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
        username = employee_res[0].get('username')

        response = requests.get(todos_url, params={"userId": employee_id})
        employee_todos = response.json()
        obj_list = []

        for i in employee_todos:
            title = f'{i.get("title")}'
            status = i.get("completed")
            obj = {"username": username, "task": title, "completed": status}
            obj_list.append(obj)

        obj_dict[employee_id] = obj_list

    # convert to json
    filename = 'todo_all_employees.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(obj_dict, f)
