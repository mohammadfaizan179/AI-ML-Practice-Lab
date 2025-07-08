import pandas as pd


def replace_interpolate():
    df = pd.read_csv("csv_2.csv")

    # print(df.replace(
    #     to_replace="male",
    #     # to_replace=["male", "Imran"],
    #     # to_replace="[A-Z]",
    #     # to_replace={"name": "Rizwan", "gender": "male"},
    #     value="MALE",
    #     inplace=False,
    #     # method="ffill",
    #     limit=3
    # ))

    print(df.interpolate())
    print(df.infer_objects(copy=False))