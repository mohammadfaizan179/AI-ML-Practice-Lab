import pandas as pd


def arithmatic_operations():
    df1 = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    df1["sum"] = df1["a"] + df1["b"]
    df1["diff"] = df1["a"] - df1["b"]
    df1["mult"] = df1["a"] * df1["b"]
    df1["divid"] = df1["b"] / df1["a"]
    df1["d > a"] = df1["b"] > df1["a"]
    df1["a > b"] = df1["a"] > df1["b"]
    df1["a > 2"] = df1["a"] > 2
    print(df1)
