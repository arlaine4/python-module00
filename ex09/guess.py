import random

ref = "The answer to the ultimate question of life"\
      "the universe and everything is 42."
win_msg = "Congratulations! You got it on your"


def print_win_msg(att, nb):
    tmp = ''
    if att == 1:
        tmp = 'first'
    elif att == 2:
        tmp = '2nd'
    elif att == 3:
        tmp = '3rd'
    else:
        tmp = str(att) + 'th'
    if nb == 42:
        print(ref)
    print(f'{win_msg} {tmp} try!')


if __name__ == "__main__":
    stop = False
    while 1:
        secret_nb = random.randint(1, 100)
        curr = None
        attempts = 0
        while curr != secret_nb:
            if attempts == 0 or curr == secret_nb:
                print("What's your guess between 1 and 99 ?",
                      "\nType 'exit' to end the game")
            else:
                print("What's your guess between 1 and 99 ?")
            curr = input()
            if curr == 'exit':
                stop = True
                break
            else:
                try:
                    curr = int(curr)
                except ValueError:
                    print("That's not a number.")
                    continue
            attempts += 1
            if curr < 0 or curr > 99:
                print("You need to enter a number between 0 and 99.")
                continue
            if curr < secret_nb:
                print("Too low!")
            elif curr > secret_nb:
                print("Too high!")
            else:
                print_win_msg(attempts, secret_nb)
        if stop is True:
            print("Goodbye!")
            break
