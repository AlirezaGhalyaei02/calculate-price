def calculate_price(price, tax_rate = 0.1):
    final_price = price * (tax_rate + 1)
    return final_price


def main():
    price = float(input())

    try:
        tax_rate = float(input())
        result = round(calculate_price(price, tax_rate))

    except:
        result = round(calculate_price(price))

    print(result)


main()