import sys

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        final = [f for f in sys.argv[1::]]
        final = " ".join(final)
        final = final[::-1].swapcase()
        print(final)
