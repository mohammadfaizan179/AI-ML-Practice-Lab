import pandas as pd


def insert_delete():
    df1 = pd.DataFrame(
        data=[[1, 2, 3, 4, 5], [6, 2, 1, 7, 9]]
    )
    print(df1)
    print()

    df1["c"] = df1[0]
    print(df1)
    print()

    df1["d"] = df1[0][1:]
    print(df1)
    print()

    df1.insert(1, "e", [11, 22])
    print(df1)
    print()

    res = df1.pop("e")
    print(res)
    print(type(res))
    print()

    del df1["d"]

    print(df1)
    print()
