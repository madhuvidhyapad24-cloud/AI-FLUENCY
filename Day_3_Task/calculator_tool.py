def calculate_fee(expression):
    return eval(expression)


if __name__ == "__main__":
    print(calculate_fee("(12000 + 18000) * 0.9"))