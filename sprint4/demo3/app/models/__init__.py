import psycopg2
import os

configs = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}

# host=os.getenv("DB_HOST") ...
conn = psycopg2.connect(**configs)
