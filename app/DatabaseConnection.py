import psycopg
import time
from psycopg import Connection
from typing import Optional


class DatabaseConnection:

    def connect(self) -> Optional[Connection]:
        attempts = 0
        while attempts < 5:
            try:
                conn = psycopg.connect(
                    dbname="miniatures-site",
                    user="postgres",
                    password="password",
                    host="postgres",
                    port="5432",
                )

                print("+++ Database connection successful +++")
                return conn

            except Exception as error:
                print("Database connection failure: ", error)
                attempts += 1
                time.sleep(3)
