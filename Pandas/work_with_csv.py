import pandas as pd
import numpy as np


def work_with_csv():
    df1 = pd.DataFrame(
        data=[
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 1],
        ]
    )
    # print(df1)

    # df1.to_csv("Datasets/csv_2.csv", index=False, header=["a", "b", "c"])

    df2 = pd.read_csv("Datasets/csv_2.csv")
    print(df2)
    print()

    # df2 = pd.read_csv("Datasets/csv_2.csv", nrows=2)
    # df2 = pd.read_csv("Datasets/csv_2.csv", nrows=20, usecols=[0])
    # df2 = pd.read_csv("Datasets/csv_2.csv", skiprows=2)
    # df2 = pd.read_csv("Datasets/csv_2.csv", header=2)
    # df2 = pd.read_csv("Datasets/csv_2.csv", names=["col1", "col2", "col3"])
    # df2 = pd.read_csv("Datasets/csv_2.csv", dtype={"a": "float"})
    # print(df2)

    # print(df2.index)
    # print(df2.describe())
    # print(df2.head(2))
    # print(df2.tail(2))
    # print(df2[:2])
    # print(df2.index.to_list())
    # print(df2.to_numpy())

    # print(np.asarray(df2))

    # print(df2.sort_index(ascending=False))

    # df2["a"][0] = 11

    # df2.loc[0, "a"] = 11

    # arr1 = df2.to_numpy()
    # print(arr1)
    # print(arr1[1:, 0:2])

    # print(df2.loc[[1,2], ["a", "b"]])
    # print(df2.loc[[1,2], :])

    # print(df2.loc[1, "a"])
    # print(df2.iloc[1, 0])

    # print(df2.loc[[1, 2], ["b", "c"]])
    # print(df2.iloc[[1, 2], [1, 2]])
