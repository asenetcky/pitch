import polars as pl
import requests 

def main():
    api = "https://data.ct.gov/resource/qhtt-czu2.csv"
    response = requests.get(api)

    response.raise_for_status()

    text = response.content
    df = pl.read_csv(source=text)

    print(df)


if __name__ == "__main__":
    main()