import pandas as pd


def data_frame():
    df1 = pd.DataFrame(
        data=[[1, 2, 3, 4, 5], ["a", "b", "c", "d", "e"]],
        index=["row1", "row2"],
        columns=["col1", "col2", "col3", "col4", "col5"]
    )
    df2 = pd.DataFrame(
        data=[
            [1, 2, 3, 4, 5],
            [11, 22, 33, 44, 55],
            [111, 222, 333, 444, 555],
        ],
    )

    # Note: DF can be created with different size lists

    df3 = pd.DataFrame(
        data=[
            [1, 2, 3, 4],
            [11, 44, 55],
            [111, 555],
        ],
    )
    # print(df2)
    # print(type(df2))

    df4 = pd.DataFrame((1, 2, 3))
    # print(df4)

    # Note: DF can't be created with different size values of keys
    df5 = pd.DataFrame({"A.Karim": (1, 2, 3), "A.Rahim": (4, 5, 6)})
    df5 = pd.DataFrame(
        data={"A.Karim": (1, 2, 3), "A.Rahim": (4, 5, 6)},
        columns=["A.Karim"]
    )
    # print(df5)

    dict1 = {"a": [1, 2, 3], "b": [4, 5, 6]}
    df6 = pd.DataFrame(dict1, columns=["a", "b"])
    # print(df6)

    s1 = pd.Series([1, 2, 3, 4, 5])
    # print(s1)

    df = pd.read_csv("Datasets/csv_3.csv")
    # print(df.head())
    # print(df.tail())
    # print(df.columns)
    # print(df.shape)
    # print(df.info())
    # print(df.describe())
    # print(df.loc[1])
    # print(df.loc[0, "name"])
    # print(df.iloc[1])

    # Filter
    # print(df[df["age"] >= 30])  # Using Boolean indexing
    # print(df.query("age > 30"))  # Using string query

