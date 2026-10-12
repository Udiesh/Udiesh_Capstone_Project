
import requests
from bs4 import BeautifulSoup


URL = "https://www.scrapethissite.com/pages/simple/"
COUNTRY_LIMIT = 20


def scrape_countries():
    """
    Scrape the first 20 countries from the target website.

    Returns:
        list[dict]: Country records containing name, capital,
                    population, and area.
    """

    # Step 1: Send a GET request
    try:
        response = requests.get(URL, timeout=15)
        response.raise_for_status()

    except requests.RequestException as error:
        raise RuntimeError(
            f"Failed to fetch country data: {error}"
        ) from error

    # Step 2: Parse the HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 3: Find country containers and select the first 20
    country_blocks = soup.select("div.country")[:COUNTRY_LIMIT]

    if len(country_blocks) != COUNTRY_LIMIT:
        raise ValueError(
            f"Expected {COUNTRY_LIMIT} countries, "
            f"but found {len(country_blocks)}."
        )

    countries = []

    # Step 4: Extract and clean each country
    for block in country_blocks:
        name_element = block.select_one(".country-name")
        capital_element = block.select_one(".country-capital")
        population_element = block.select_one(".country-population")
        area_element = block.select_one(".country-area")

        if not all([
            name_element,
            capital_element,
            population_element,
            area_element,
        ]):
            raise ValueError(
                "A country record is missing one or more required fields."
            )

        name = name_element.get_text(strip=True)
        capital = capital_element.get_text(strip=True)
        population_text = population_element.get_text(strip=True)
        area_text = area_element.get_text(strip=True)

        # Step 5: Convert values to the required numeric types
        population = int(population_text)
        area = float(area_text)

        # Step 6: Store the record as a dictionary
        country = {
            "name": name,
            "capital": capital,
            "population": population,
            "area": area,
        }

        countries.append(country)

    return countries


# Run this section only when executing scraper.py directly
if __name__ == "__main__":
    try:
        country_data = scrape_countries()

        print(f"Successfully scraped {len(country_data)} countries.\n")

        for country in country_data:
            print(country)

        print("\nData types of the first record:")

        if country_data:
            for field, value in country_data[0].items():
                print(f"{field}: {type(value).__name__}")

    except (RuntimeError, ValueError, TypeError) as error:
        print(f"Scraping error: {error}")
