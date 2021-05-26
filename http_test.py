#!/usr/bin/env python3

import requests
from pprint import pprint

SEPARATOR = "/"
HOST = "http://127.0.0.1:5000"
USER = "user"
USERS = USER + "s"
URL_USERS = HOST + SEPARATOR + USERS
URL_USER = HOST + SEPARATOR + USER
URL_USER_CREATE = URL_USER + SEPARATOR + "create" 
URL_USERS_UPDATE = URL_USER + SEPARATOR + "update" 

def scan():
  print("Scan Request: ")
  out = requests.get(URL_USERS)
  pprint(out.json())

def create():
  print("Create requests:")
  test_data = {
    "first_name" : "John",
    "last_name" : "Doe",
    "hobbies" : "Fishing"
  }
  out = requests.post(URL_USER_CREATE, json=test_data)
  pprint(out.json())

def update():
  print("Update requests:")
  test_data = {
    "id" : "2",
    "hobbies" : "Opera Singing"
  }
  out = requests.post(URL_USERS_UPDATE, json=test_data)
  pprint(out.json())

if __name__ == "__main__":
  update()
  scan()
