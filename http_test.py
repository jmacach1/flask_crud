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
URL_USER_UPDATE = URL_USER + SEPARATOR + "update"
URL_USER_DELETE = URL_USER + SEPARATOR + "delete"  

def scan():
  print("Scan Request: ")
  out = requests.get(URL_USERS)
  pprint(out.json())
  print("\n")

def create():
  print("Create requests:")
  test_data = {
    "first_name" : "Jabba",
    "last_name" : "Wockeez",
    "hobbies" : "Breakdancing"
  }
  out = requests.post(URL_USER_CREATE, json=test_data)
  pprint(out.json())
  print("\n")

def update(id):
  print("\nUpdate requests:")
  test_data = {
    "id" : str(id),
    "hobbies" : "Freestyle Jamming"
  }
  out = requests.put(URL_USER_UPDATE, json=test_data)
  pprint(out.json())
  print("\n")


def delete(id):
  print("\nDelete requests:")
  test_data = { 
    id: str(id)
  }
  out = requests.delete(URL_USER_DELETE + SEPARATOR + test_data[id])
  pprint(out.json())

if __name__ == "__main__":
  scan()

  print("\nExpected - UPDATE - User 7 not found")
  update(7)
  print("\nExpected - DELETE - User 7 not found")
  delete(7) # not found 
  scan()
  
  print("\nExpected - CREATE - User 7 created")
  create() # create user 7
  scan()

  print("\nExpected - UPDATE - Success")
  update(7) # update user 7
  scan() 
  
  print("\nExpected - DELETE - Success")
  delete(7) # delete user 7
  scan()