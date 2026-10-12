# Country Data Pipeline & Analytics

An end-to-end Python project that scrapes data for the first 20 countries from [Scrape This Site](https://www.scrapethissite.com/pages/simple/), stores it in SQLite, exposes it through a FastAPI REST API, and generates a CSV export and scatter plot.

## Features

- Web scraping using Requests and BeautifulSoup
- SQLite database with country name as the primary key
- Object-oriented database management with CRUD operations
- REST API built with FastAPI
- Data retrieval and CSV export using Pandas
- Population vs. area scatter plot using Matplotlib

## Project Structure

| File | Purpose |
|---|---|
| `scraper.py` | Fetches the webpage and extracts the first 20 countries, including their names, capitals, populations, and areas. |
| `database.py` | Defines `CountryDatabaseManager`, which creates the SQLite table and handles database operations: insert, read, update, and delete. |
| `seed.py` | Runs the scraper and inserts the scraped records into `countries.db`. Existing country names are skipped. |
| `main.py` | Implements the FastAPI application and its five REST endpoints for managing country records. |
| `client.py` | Fetches country data from the API, displays it as a Pandas DataFrame, exports a CSV file, and generates the scatter plot. |
| `requirements.txt` | Lists the Python packages required to run the project. |
| `.gitignore` | Specifies local files and generated artifacts that Git should ignore. |

### Files generated at runtime

| File | Purpose |
|---|---|
| `countries.db` | SQLite database containing country records. |
| `exported_countries.csv` | CSV export of the data retrieved through the API. |
| `population_vs_area.png` | Scatter plot comparing country population and area. |

These files are generated locally and do not need to be committed to GitHub.

## Prerequisites

- Python 3.10 or later
- Internet connection to scrape the source website
- A terminal such as Windows CMD, PowerShell, or a Unix shell

## Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

Replace the placeholders with your GitHub repository URL and folder name.

### 2. Create and activate a virtual environment

**Windows CMD**

```cmd
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Run the Project

Follow these steps in order.

### Step 1: Populate the database

```bash
python seed.py
```

This scrapes the first 20 countries and inserts them into `countries.db`.

On the first run, you should see 20 records inserted. If you run the script again, existing country names are skipped rather than duplicated.

### Step 2: Start the API

```bash
uvicorn main:app --reload
```

Keep this terminal running while using the API.

Open the interactive API documentation in your browser:

**http://127.0.0.1:8000/docs**

### Step 3: Run the client

Open a second terminal, navigate to the project directory, and activate the virtual environment again if necessary.

```bash
python client.py
```

The client retrieves data from the running API, prints the results, and generates:

- `exported_countries.csv`
- `population_vs_area.png`

Both files are saved in the client's current working directory.

## API Endpoints

The API runs locally at `http://127.0.0.1:8000`.

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/countries` | Retrieve all countries. |
| `GET` | `/countries/{country_name}` | Retrieve a country by name. |
| `POST` | `/countries` | Create a new country. |
| `PUT` | `/countries/{country_name}` | Update an existing country. |
| `DELETE` | `/countries/{country_name}` | Delete a country by name. |

The API validates incoming data and returns appropriate HTTP status codes for successful operations, missing records, and duplicate country names.

## Database Notes

- The project uses SQLite, so no separate database server is required.
- The database file is created locally when the database manager initializes.
- Country names are used as the primary key.
- The database persists between application runs.
- Each local installation maintains its own database file.

To rebuild the database from scratch, stop the API, delete `countries.db`, and run `python seed.py` again. **This permanently removes the existing local database and its records.**

## Tech Stack

Python · Requests · BeautifulSoup · SQLite · FastAPI · Pydantic · Pandas · Matplotlib

