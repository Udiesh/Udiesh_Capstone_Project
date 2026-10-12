
import requests
import pandas as pd
import matplotlib.pyplot as plt

API_URL = "http://127.0.0.1:8000/countries"


def fetch_countries():
    response = requests.get(API_URL, timeout=15)
    response.raise_for_status()
    return response.json()


def main():
    try:
        countries = fetch_countries()

        if not countries:
            print("No countries found in the API.")
            return

        df = pd.DataFrame(countries)

        print("\nCountry Data:")
        print(df.to_string(index=False))

        df.to_csv("exported_countries.csv", index=False)

        


        plt.figure(figsize=(10, 6))

        plt.scatter(
            df["population"],
            df["area"],
            alpha=0.7
        )

        plt.title("Population vs Area of Countries")
        plt.xlabel("Population")
        plt.ylabel("Area (sq. km)")
        plt.grid(True, linestyle="--", alpha=0.5)

        plt.tight_layout()
        plt.savefig("population_vs_area.png", dpi=300)
        plt.close()

        print("Scatter plot saved: population_vs_area.png")


        print("\nCSV exported successfully: exported_countries.csv")

    except requests.RequestException as error:
        print(f"API request failed: {error}")


if __name__ == "__main__":
    main()
