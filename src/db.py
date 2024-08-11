import sqlalchemy
from sqlalchemy.sql import text
import psycopg2

def connect_db(host: str, user: str, password: str, db_name: str, port: int = 5433) -> sqlalchemy.engine.Engine:
    try:
        connection_engine = sqlalchemy.create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}")
        return connection_engine
    except psycopg2.errors.ConnectionException as exc:
        print(exc)
        exit()


def insert_into_db(values: dict, table: str):
    placeholders_with_column_names = ', '.join([f"{x}" for x in values.keys()])
    placeholders_value_bings = ', '.join([f":{x} " for x in values.keys()])
    stmt = text(f"INSERT INTO {table}({placeholders_with_column_names}) VALUES ({placeholders_value_bings})")
    connection = connect_db("localhost", "realtime", "realtime", "realtime", 5433)
    conn = connection.connect()
    try:
        conn.execute(stmt, values)
        conn.commit()
    except Exception as exc:
        print(exc)
    finally:
        conn.close()
