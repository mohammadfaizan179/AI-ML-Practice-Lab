import pandas as pd


def drop_fill():

    df = pd.read_csv("Datasets/csv_2.csv")
    print(df.dropna(
        axis=0,
        how="any",
        subset=["age"],
        # thresh=3,
        inplace=False,
        ignore_index=False
    ))

    print(df.fillna(
        value="PYTHON",
        # value={"gender": "Test1", "age": 99},
        # axis=2,
        # limit=2,
        # method="ffill",
        inplace=False
    ))
    df = pd.read_csv("Datasets/csv_3.csv")
    print(df.fillna(
        value={"age": "*", "gender": "#"},
    ))
    print(df.fillna("*"))

    print(df.fillna(
        value={"age": df["age"].mean()}
    ))
    print(df["age"].fillna(df["age"].mean()))

    print(df.fillna(method="bfill"))