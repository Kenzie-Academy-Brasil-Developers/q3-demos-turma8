from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["db_test"]


class User:
    def __init__(self, name, last_name, email, country, password):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.country = country
        self.password = password

    def save(self):
        db.users.insert_one(self.__dict__)
        del self._id

        return self.__dict__

    @staticmethod
    def find_all():
        users = list(db.users.find())

        for user in users:
            del user["_id"]

        return users

    @staticmethod
    def update_user(email, data):
        db.users.update_one({"email": email}, {"$set": data})
        user = db.users.find_one({"email": email})

        del user["_id"]

        return user

    @staticmethod
    def delete_user(email):
        user = db.users.find_one_and_delete({"email": email})

        del user["_id"]

        return user
