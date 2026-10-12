
import sqlite3
from pathlib import Path
from contextlib import closing

DB_PATH = Path(__file__).resolve().parent / "countries.db"


class CountryDatabaseManager:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        self.create_table()

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def create_table(self):
        with closing(self.get_connection()) as conn:
            with conn:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS countries (
                        name TEXT PRIMARY KEY,
                        capital TEXT NOT NULL,
                        population INTEGER NOT NULL,
                        area REAL NOT NULL
                    )
                """)

    def insert_country(self, country):
        with closing(self.get_connection()) as conn:
            with conn:
                conn.execute("""
                    INSERT INTO countries (name, capital, population, area)
                    VALUES (?, ?, ?, ?)
                """, (
                    country["name"],
                    country["capital"],
                    country["population"],
                    country["area"]
                ))
        return True

    def get_all_countries(self):
        with closing(self.get_connection()) as conn:
            with conn:
                conn.row_factory = sqlite3.Row
                rows = conn.execute("""
                    SELECT name, capital, population, area
                    FROM countries
                    ORDER BY name
                """).fetchall()
                return [dict(row) for row in rows]

    def get_country(self, name):
        with closing(self.get_connection()) as conn:
            with conn:
                conn.row_factory = sqlite3.Row
                row = conn.execute("""
                    SELECT name, capital, population, area
                    FROM countries
                    WHERE name = ?
                """, (name,)).fetchone()
                return dict(row) if row else None

    def update_country(self, name, updated_data):
        with closing(self.get_connection()) as conn:
            with conn:
                cursor = conn.execute("""
                    UPDATE countries
                    SET capital = ?, population = ?, area = ?
                    WHERE name = ?
                """, (
                    updated_data["capital"],
                    updated_data["population"],
                    updated_data["area"],
                    name
                ))
                return cursor.rowcount > 0

    def delete_country(self, name):
        with closing(self.get_connection()) as conn:
            with conn:
                cursor = conn.execute("""
                    DELETE FROM countries
                    WHERE name = ?
                """, (name,))
                return cursor.rowcount > 0
