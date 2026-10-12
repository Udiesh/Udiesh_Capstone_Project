
from database import CountryDatabaseManager

# Use a separate database so the real dataset remains untouched
db = CountryDatabaseManager("test_countries.db")

# CREATE
country = {
    "name": "Testland",
    "capital": "Test City",
    "population": 100000,
    "area": 250.5,
}

db.insert_country(country)
print("Inserted:", db.get_country("Testland"))

# READ ALL
print("All countries:", db.get_all_countries())

# UPDATE
updated_country = {
    "capital": "New Test City",
    "population": 120000,
    "area": 300.0,
}

success = db.update_country("Testland", updated_country)
print("Update successful:", success)
print("After update:", db.get_country("Testland"))

# DELETE
success = db.delete_country("Testland")
print("Delete successful:", success)
print("After delete:", db.get_country("Testland"))
