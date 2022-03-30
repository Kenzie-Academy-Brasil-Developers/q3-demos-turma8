import psycopg2
import os
from psycopg2 import sql

# 1. Gerenciador de contexto WITH
# 2. Criar uma funcao que retorne uma nova connection sempre que necessário
# 3. Utilizar herança POO para conexao


configs = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}


class DatabaseConnector:
    @classmethod
    def get_conn_cur(cls):
        cls.conn = psycopg2.connect(**configs)
        cls.cur = cls.conn.cursor()

        # Exemplo de composição slido
        # return cls.conn, cls.cur

    @classmethod
    def commit_and_close(cls):
        cls.conn.commit()
        cls.cur.close()
        cls.conn.close()

    @classmethod
    def select_all(cls, table_name: str):
        cls.get_conn_cur()

        sql_table_name = sql.Identifier(table_name)

        query = sql.SQL(
            """
                SELECT * FROM {table}
            """
        ).format(table=sql_table_name)

        cls.cur.execute(query)

        result = cls.cur.fetchall()

        print("=" * 100)
        print(query.as_string(cls.cur))
        print("=" * 100)

        cls.commit_and_close()

        return result

    @classmethod
    def serialize(cls, values: tuple, columns: list[str]):
        return dict(zip(columns, values))
