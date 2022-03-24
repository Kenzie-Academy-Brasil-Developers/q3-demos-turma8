from app.models import DatabaseConnector


class User(DatabaseConnector):
    def __init__(self, **kwargs):
        self.email = kwargs["email"]
        self.birthdate = kwargs["birthdate"]
        self.children = kwargs["children"]
        self.married = kwargs["married"]
        self.account_balance = kwargs["account_balance"]

    @classmethod
    def read_users(cls):
        # Cria os atributos conn e cur na classe Pai (DatabaseConector)
        cls.get_conn_cur()

        query = "SELECT * FROM users;"

        cls.cur.execute(query)

        users = cls.cur.fetchall()

        cls.cur.close()
        cls.conn.close()

        return users

    def create_user(self):
        # Exemplo de composição do slido
        # conn, cur = DatabaseConnector.get_conn_cur()

        self.get_conn_cur()

        query = """
            INSERT INTO users
                (email, birthdate, children, married, account_balance)
            VALUES
                (%s, %s, %s, %s, %s)
            RETURNING *
        """

        query_values = tuple(self.__dict__.values())
        # print(f"{query_values=}")

        self.cur.execute(query, query_values)
        # print(f"{self.cur.query=}")

        # Registro persiste no banco
        self.conn.commit()

        inserted_user = self.cur.fetchone()

        self.cur.close()
        self.conn.close()

        return inserted_user
