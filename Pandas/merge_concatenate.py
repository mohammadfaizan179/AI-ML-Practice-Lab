import pandas as pd


def merge_concatenate():
    df1 = pd.DataFrame(
        data=[
            [1, 2, 3, 4, 5],
            [11, 22, 33, 44, 55],
            [111, 222, 333, 444, 555],
        ],
        index=["row1", "row2", "row3"],
        columns=["co"
                 "l1", "col2", "col3", "col4", "col5"],
    )

    df2 = pd.DataFrame([
        [1, 2, 3],
        [4, 5, 6],
    ])
    print(df1 + df2)
