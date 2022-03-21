import pymongo
from typing import Union
from bson.objectid import ObjectId
import re
from pymongo import ReturnDocument


from app.exceptions.dev_exc import DevIdNotFound

# Database URI/URL
client = pymongo.MongoClient("mongodb://localhost:27017/")


# use turma8
db = client["turma8"]

# db.colecao

db.create_collection("minha_colecao")


class Dev:
    def __init__(self, name, email, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        self.name = kwargs["name"]
        self.email = kwargs["email"]
        self.age = kwargs.get("age", 100)

    @staticmethod
    def serialize_dev(dev: Union["Dev", dict]):
        if type(dev) is dict:
            dev.update({"_id": str(dev["_id"])})
        elif type(dev) is Dev:
            dev._id = str(dev._id)

        return dev

    @staticmethod
    def get_all():
        devs_list = db.devs.find()

        return devs_list

    def create_dev(self):
        db.devs.insert_one(self.__dict__)

    @staticmethod
    def delete_dev(dev_id: str):
        # db.devs.find_one(filtro de id)
        # db.devs.delete_one()

        deleted_dev = db.devs.find_one_and_delete({"_id": ObjectId(dev_id)})
        print(f"{type(deleted_dev)}")
        print(f"{deleted_dev}")

        return deleted_dev

    @staticmethod
    def filter_by_gmail():
        # /@gmail/
        gmail_regex = re.compile("@gmail")

        devs = db.devs.find({"email": gmail_regex})

        return devs

    @staticmethod
    def update_dev(dev_id: str, payload: dict):
        updated_dev = db.devs.find_one_and_update(
            {"_id": ObjectId(dev_id)},
            {"$set": payload},
            return_document=ReturnDocument.AFTER,
        )

        if not updated_dev:
            raise DevIdNotFound

        return updated_dev
