import pandas as pd


def get_placement_payment_breakdown(
        payment_method,
        due_amount: float,
        order_total: str,
        total_discount,
        order_total_without_discount,
        merchant_fee: float = 0,
        service_fee: float = 0,
        currency: str = "PKR",
) -> bool:
    print("Testing.....payment_method", payment_method)
    print("Testing.....due_amount", due_amount)
    print("Testing.....order_total", order_total)
    print("Testing.....total_discount", total_discount)
    print("Testing.....order_total_without_discount", order_total_without_discount)
    print("Testing.....merchant_fee", merchant_fee)
    print("Testing.....service_fee", service_fee)
    print("Testing.....currency", currency)
    return True


def drop_fill():

    get_placement_payment_breakdown(
        "Strip",
        12.12,
        "11.11",
        12.13,
        12.14,
        currency="PKR"
    )

    # df = pd.read_csv("csv_2.csv")
    # print(df, end="\n\n")
    #
    # print(df.dropna())

    # print(df.dropna(how="all"), end="\n\n")
    # print(df.dropna(how="any"), end="\n\n")
