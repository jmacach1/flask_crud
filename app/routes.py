# http routes

from flask import request
from app import app
from app.database import (scan, findOne, create, update, delete)

@app.route("/users")
def get_all_users():
  users = scan()
  return {
    "ok": True,
    "message": "Success",
    "users": users
  }

@app.route("/user/<int:id>")
def get_user(id):
  user = findOne(id)
  return {
    "ok": True,
    "message": "Success",
    "user": user
  }


@app.route("/user/create", methods=["POST"])
def create_user(): # view fn
  user_data = request.json
  new_id = create(
    user_data.get("first_name"),
    user_data.get("last_name") ,
    user_data.get("hobbies")
  )
  return {
    "ok" : True,
    "message": "Success",
    "new_id" : new_id
  }


@app.route("/user/update", methods=["PUT"])
def update_user():
  user_data = request.json
  id = user_data.get("id")
  user = update(
    id,
    user_data.get("first_name"),
    user_data.get("last_name"),
    user_data.get("hobbies")
  )
  if user:
    return {
      "ok" : True,
      "message": "Success",
      "new_id" : user
    }
  return {
    "ok": False,
    "message": f"Unable to Update user {id} not Found"
  }



@app.route("/user/delete/<int:id>", methods=["DELETE"])
def delete_user(id):
  message = delete(id)
  return {
    "message": message
  }


###########

# @app.route('/user/<name>')
# def user(name):
#   return f"<h1> Hello, {name}</h1>"

@app.route('/square/<int:number>')
def square(number):
  return f"<h1>{str(number)} squared is {str(number**2)} </h1>"

@app.route('/agent')
def agent():
  user_agent = request.headers.get("User-Agent")
  return f"<p>Your user agent is {user_agent}</p>"