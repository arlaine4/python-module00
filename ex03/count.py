import string
import inspect


def text_analyzer(*args):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    base = "At this time you are sleeping ? It's not possible!"
    if len(args) > 1:
        print('ERROR')
        return
    try:
        text = args[0] if len(args[0]) != 0 else base
    except IndexError:
        text = base
        print('What is the text to analyse?')
        print(">>", text)
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    spaces = sum(1 for c in text if c == ' ')
    punc = sum(1 for c in text if c in string.punctuation)
    len_ = len(text)
    s = (f"This text contains {len_} characters:\n",
         f"- {upper} upper letters\n",
         f"- {lower} lower letters\n",
         f"- {punc} punctuation marks\n",
         f"- {spaces} spaces\n")
    print("{}{:<1}{:<1}{:<1}{:<1}".format(s[0], s[1], s[2],
                                          s[3], s[4]))
