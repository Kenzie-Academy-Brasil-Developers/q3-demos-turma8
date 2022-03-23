from app.models import conn


class User:
    def __init__(self, **kwargs):
        self.email = kwargs["email"]
        self.birthdate = kwargs["birthdate"]
        self.children = kwargs["children"]
        self.married = kwargs["married"]
        self.account_balance = kwargs["account_balance"]

    @staticmethod
    def read_users():
        cur = conn.cursor()

        query = "SELECT * FROM users;"

        cur.execute(query)

        users = cur.fetchall()

        return users
