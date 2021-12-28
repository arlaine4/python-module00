from decimal import Decimal


if __name__ == "__main__":
    t = (0, 4, 132.42222, 10000, 12345.67)
    lasts = (Decimal(t[3]), Decimal(t[4]))
    print("module_{:0>2}".format(t[0]), end=', ')
    print("ex_{:0>2}".format(t[1]), end=' : ')
    print("{:.2f}".format(t[2]), end=', ')
    print("{:.2e}".format(t[3]), end=', ')
    print("{:.2e}".format(t[4]))
