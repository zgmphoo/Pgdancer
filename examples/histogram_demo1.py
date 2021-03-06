import pandas as pd


from pgdancer import histogram


if __name__ == '__main__':
    # example code
    df = pd.read_csv("brands_data.csv", index_col="brands", thousands=",").fillna(0)
    df = df.astype("int")
    h = histogram.Histogram(df, 1600, 900, window_type=0)
    h.run("pgdancer", "Top 15 Best Global Brands Ranking", "---Datasource:https://www.interbrand.com", \
          "Top 15 Best Global Brands Ranking", "Brand Value:$m")

