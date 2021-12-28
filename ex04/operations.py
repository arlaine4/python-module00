import argparse


def args_parsing():
    usage_msg = "python operations.py <number1> <number2>"
    example_msg = "Example:\n   python operations.py 10 3"
    parser = argparse.ArgumentParser(usage=usage_msg + '\n'
                                     + example_msg)
    parser.add_argument('number1', type=int)
    parser.add_argument('number2', type=int)
    options = parser.parse_args()
    return options


def add(nb1, nb2):
    return nb1 + nb2


def sub(nb1, nb2):
    return nb1 - nb2


def mult(nb1, nb2):
    return nb1 * nb2


def div(nb1, nb2):
    if nb2 == 0:
        return "ERROR (div by zero)"
    else:
        return nb1 / nb2


def modulo(nb1, nb2):
    if nb2 == 0:
        return "ERROR (modulo by zero)"
    else:
        return nb1 % nb2


def get_res(nb1, nb2):
    res = []
    res.append(add(nb1, nb2))
    res.append(sub(nb1, nb2))
    res.append(mult(nb1, nb2))
    res.append(div(nb1, nb2))
    res.append(modulo(nb1, nb2))
    return res


def print_result(res):
    print("Sum:\t   ", res[0])
    print("Difference:", res[1])
    print("Product:   ", res[2])
    print("Quotient:  ", res[3])
    print("Remainder: ", res[4])


if __name__ == "__main__":
    args = args_parsing()
    res = get_res(args.number1, args.number2)
    print_result(res)
