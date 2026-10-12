
import sqlite3

from scraper import scrape_countries
from database import CountryDatabaseManager


def seed_database():
    db = CountryDatabaseManager()
    countries = scrape_countries()

    inserted_count = 0
    skipped_count = 0

    for country in countries:
        try:
            db.insert_country(country)
            inserted_count += 1

        except sqlite3.IntegrityError:
            print(f"Already exists, skipping: {country['name']}")
            skipped_count += 1

    print("\nSeeding completed.")
    print(f"New records inserted: {inserted_count}")
    print(f"Existing records skipped: {skipped_count}")
    print(f"Total records in database: {len(db.get_all_countries())}")


if __name__ == "__main__":
    seed_database()
