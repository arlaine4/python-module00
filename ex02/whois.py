import sys

if __name__ == "__main__":
    if len(sys.argv) > 2:
        sys.exit("ERROR")
    elif len(sys.argv) == 1:
        sys.exit()
    else:
        try:
            nb = int(sys.argv[1])
        except ValueError:
            sys.exit('ERROR')
        if nb != 0:
            print("I'm Even." if nb % 2 == 0 else "I'm Odd.")
        else:
            print("I'm Zero.")
