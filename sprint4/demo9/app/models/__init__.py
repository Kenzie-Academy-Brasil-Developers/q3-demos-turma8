import psycopg2
import os
from psycopg2 import sql, extras

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
    DEC2FLOAT = psycopg2.extensions.new_type(
        psycopg2.extensions.DECIMAL.values,
        "DEC2FLOAT",
        lambda value, curs: float(value) if value is not None else None,
    )
    psycopg2.extensions.register_type(DEC2FLOAT)

    @classmethod
    def get_conn_cur(cls):
        cls.conn = psycopg2.connect(**configs)
        cls.cur = cls.conn.cursor(cursor_factory=extras.RealDictCursor)

        # Exemplo de composição slido
        # return cls.conn, cls.cur

    @classmethod
    def commit_and_close(cls, commit=True):
        if commit:
            cls.conn.commit()
        cls.cur.close()
        cls.conn.close()

    @classmethod
    def insert_into(cls, payload: dict, table_name: str):
        cls.get_conn_cur()

        sql_table_name = sql.Identifier(table_name)
        columns = [sql.Identifier(key) for key in payload.keys()]
        values = [sql.Literal(value) for value in payload.values()]

        query = sql.SQL(
            """
                INSERT INTO {table}
                    ({columns})
                VALUES
                    ({values})
                RETURNING *
            """
        ).format(
            table=sql_table_name,
            columns=sql.SQL(",").join(columns),
            values=sql.SQL(",").join(values),
        )

        cls.cur.execute(query)

        result = cls.cur.fetchone()

        cls.commit_and_close()

        return result

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
