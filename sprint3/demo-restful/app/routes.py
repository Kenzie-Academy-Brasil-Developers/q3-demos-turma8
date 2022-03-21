from flask import current_app, request, jsonify, abort, url_for
from .models import User
import requests as r


validated_users = []


# VERIFY USER
@current_app.post("/validate")
def validateUser():
    data = request.get_json()

    validated_users.append(data["email"])

    try:
        user = User(**data)
        validated_users.append(data["email"])
        return jsonify(user.__dict__), 200
    except:
        abort(400)


# CREATE
@current_app.post("/createUser")
def createUser():

    data = request.get_json()

    if data["email"] not in validated_users:
        return {"msg": "user not validated yet"}, 400

    try:
        user = User(**data)
        user.save()
        return jsonify(user.__dict__), 201
    except:
        abort(400)


# READ
@current_app.post("/users")
def get_users():
    try:
        country_api = request.args.get("country_api")
        users = User.find_all()

        data = []
        for user in users:
            country = user["country"]
            user["country"] = r.get(f"{country_api}{country}").json()
            data.append(user)

        return jsonify(data), 200
    except:
        abort(400)


# UPDATE
@current_app.post("/update/users")
def updateUser():

    try:
        data = request.get_json()
        user = User.update_user(data["email"], data)
    except:
        abort(400)

    return jsonify(user), 200


# DELETE
@current_app.post("/delete")
def deleteFromCollection():

    email = request.args.get("email")

    try:
        user = User.delete_user(email)
        return jsonify(user), 200
    except:
        abort(400)


# VIEW
# @current_app.get("/")
# def index():
#     users = User.query.all()
#     users = [item.serialized["email"] for item in users]
#     return render_template("index.html"), 200
