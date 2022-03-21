import pymongo

# Database URI/URL
client = pymongo.MongoClient("mongodb://localhost:27017/")


# use turma8
db = client["test_turma8"]


class Dev:
    @staticmethod
    def get_all():
        devs_list = db.devs.find()

        return devs_list

    """
        TODO:
        - Adicionar método de inserção
        - Adicionar método de deleção
    """

    # Inserção (tem de criar __init__ na classe)
    def create_dev(self):
        ...

    @staticmethod
    def delete_dev(dev_id: str):
        ...
