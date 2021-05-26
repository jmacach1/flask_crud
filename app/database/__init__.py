#!/usr/bin/env python3
# """Database operations"""

from flask import g # context; global
import sqlite3

ID = "id"
FIRST_NAME = "first_name"
LAST_NAME = "last_name"
HOBBIES = "hobbies"

DATABASE="user_db" # database filename

def get_db():
  db = getattr(g, "_database", None) # None is the default
  if not db:
    db = g._database = sqlite3.connect(DATABASE)
  return db

def output_formatter(results: tuple):
  out = []
  for result in results:
    res_dict = {}
    res_dict[ID] = result[0]
    res_dict[FIRST_NAME] = result[1]
    res_dict[LAST_NAME] = result[2]
    res_dict[HOBBIES] = result[3]
    out.append(res_dict)
  return out

def scan():
  cursor = get_db().execute("SELECT * FROM user", ())
  results = cursor.fetchall()
  cursor.close()
  return output_formatter(results)

def create(first_name, last_name, hobbies):
  value_tuple = (first_name, last_name, hobbies)
  query = """ 
    INSERT into user (first_name, last_name, hobbies) VALUES (?,?,?)
  """
  cursor = get_db()
  last_row_id = cursor.execute(query, value_tuple).lastrowid
  cursor.commit()
  return last_row_id


def findOne(id):
  cursor = get_db().execute("SELECT * FROM user WHERE id = ?", (str(id)))
  result = cursor.fetchone()
  if not result:
    return None
  
  return {
    ID : result[0],
    FIRST_NAME : result[1],
    LAST_NAME : result[2],
    HOBBIES : result[3]
  }

def update(id, first_name, last_name, hobbies):
  user = findOne(id)
  first_name = first_name or user[FIRST_NAME]
  last_name = last_name or user[LAST_NAME]
  hobbies = hobbies or user[HOBBIES]

  parameters = (first_name, last_name, hobbies, id)
  query = """ 
      UPDATE user
      SET 
        first_name = ?,
        last_name = ?,
        hobbies = ?
      WHERE
        id = ?
    """
  cursor = get_db()
  cursor.execute(query, parameters)
  cursor.commit()
  return findOne(id)
   
