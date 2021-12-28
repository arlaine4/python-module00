import argparse
import string


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('sentence')
    parser.add_argument('size', type=int)
    options = parser.parse_args()
    return options


if __name__ == "__main__":
    options = parse_arguments()
    s = options.sentence
    n = options.size
    res = [f for f in s.split(' ') if len(f) > n]
    for i in range(len(res)):
        for charac in res[i]:
            if charac in string.punctuation:
                res[i] = res[i].replace(charac, '')
    print(res)
