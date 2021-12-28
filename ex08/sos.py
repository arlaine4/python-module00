import sys

dic = {'A': '.-', 'B': '-...', 'C': '-.-.',
       'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
       'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
       'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
       'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
       'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
       'X': '-..-', 'Y': '-.---', 'Z': '--..',
       '0': '-----', '1': '.----', '2': '..---',
       '3': '...--', '4': '....-', '5': '.....',
       '6': '-....', '7': '--...', '8': '---..',
       '9': '----.'}


if __name__ == "__main__":
    words = [w for w in sys.argv[1:]]
    if not words:
        sys.exit()
    res = ''
    for i, word in enumerate(words):
        word = word.upper()
        for c in word:
            if c != ' ':
                try:
                    res += dic[c] + ' '
                except KeyError:
                    sys.exit("ERROR")
            elif c == ' ':
                res += ' / '
        if i < len(words) - 1:
            res += ' / '
    print(res)
