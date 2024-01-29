#!/usr/bin/python3
""" a Python script that, using this REST API"""


import requests
from sys import argv

# make a request for an employee with query string employee's id
employee_url = 'https://jsonplaceholder.typicode.com/users'
employee_todos = 'https://jsonplaceholder.typicode.com/todos'
if argv[1]:
    employee_id = argv[1]

response = requests.get(employee_url, params={"id": employee_id})
employee_res = response.json()
employee_name = employee_res[0].get('name')

response = requests.get(employee_todos, params={"userId": employee_id})
employee_todos = response.json()
TOTAL_NUMBER_OF_TASKS = len(employee_todos)
NUMBER_OF_DONE_TASKS = 0
COMPLETED_TASKS = []

for i in employee_todos:
    if i.get("completed"):
        NUMBER_OF_DONE_TASKS += 1
        COMPLETED_TASKS.append(i)

print(f"Employee {employee_name} is done with tasks({NUMBER_OF_DONE_TASKS}"
      f"/{TOTAL_NUMBER_OF_TASKS}):")

for i in COMPLETED_TASKS:
    print(f"\t {i.get('title')}")
