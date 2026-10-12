
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import sqlite3

from database import CountryDatabaseManager


app = FastAPI(
    title="Country Data API",
    description="API for managing country information",
    version="1.0.0",
)

db = CountryDatabaseManager()


class Country(BaseModel):
    name: str = Field(min_length=1)
    capital: str = Field(min_length=1)
    population: int = Field(ge=0)
    area: float = Field(ge=0)


class CountryUpdate(BaseModel):
    capital: str = Field(min_length=1)
    population: int = Field(ge=0)
    area: float = Field(ge=0)


# GET: Retrieve all countries
@app.get("/countries")
def get_countries():
    return db.get_all_countries()


# GET: Retrieve one country by name
@app.get("/countries/{country_name}")
def get_country(country_name: str):
    country = db.get_country(country_name)

    if country is None:
        raise HTTPException(
            status_code=404,
            detail="Country not found",
        )

    return country


# POST: Create a country
@app.post("/countries", status_code=201)
def create_country(country: Country):
    try:
        db.insert_country(country.model_dump())

    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Country already exists",
        )

    return db.get_country(country.name)


# PUT: Update an existing country
@app.put("/countries/{country_name}")
def update_country(country_name: str, country: CountryUpdate):
    existing_country = db.get_country(country_name)

    if existing_country is None:
        raise HTTPException(
            status_code=404,
            detail="Country not found",
        )

    db.update_country(
        country_name,
        country.model_dump(),
    )

    return db.get_country(country_name)


# DELETE: Delete a country
@app.delete("/countries/{country_name}")
def delete_country(country_name: str):
    deleted = db.delete_country(country_name)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Country not found",
        )

    return {
        "message": f"{country_name} deleted successfully"
    }
