from app.models import DatabaseConnector
from psycopg2 import sql


class User(DatabaseConnector):
    table_name = "users"

    def __init__(self, **kwargs):
        self.email = kwargs["email"]
        self.birthdate = kwargs["birthdate"]
        self.children = kwargs["children"]
        self.married = kwargs["married"]
        self.account_balance = kwargs["account_balance"]

    @classmethod
    def select_all(cls):
        return super().select_all(cls.table_name)

    def insert_into(self):
        return super().insert_into(self.__dict__, self.table_name)

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

    @classmethod
    def update_user(cls, user_id: str, payload: dict):
        cls.get_conn_cur()

        columns = [sql.Identifier(key) for key in payload.keys()]
        values = [sql.Literal(value) for value in payload.values()]
        sql_user_id = sql.Literal(user_id)

        query = sql.SQL(
            """
            UPDATE
                users
            SET
                ({columns}) = ROW({values})
            WHERE
                id = {id}
            RETURNING *;
            """
        ).format(
            id=sql_user_id,
            columns=sql.SQL(",").join(columns),
            values=sql.SQL(",").join(values),
        )

        print("=" * 100)
        print(query.as_string(cls.cur))
        print("=" * 100)

        cls.cur.execute(query)

        updated_user = cls.cur.fetchone()

        cls.commit_and_close()

        return updated_user

    @classmethod
    def read_users_by_email(cls, email: str):
        cls.get_conn_cur()

        # QUERY ERRADA
        query = f"SELECT * FROM users WHERE email LIKE '%{email}%';"

        print("=" * 100)
        print(f"{query=}")
        print("=" * 100)

        cls.cur.execute(query)

        users = cls.cur.fetchall()

        cls.commit_and_close()

        return users
