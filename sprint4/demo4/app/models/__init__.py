import psycopg2
import os

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
