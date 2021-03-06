import sys


def to_binary(text):
    binary_text = ""
    for char in text:
        binary_text += bin(ord(char))[2:].zfill(7)
    return binary_text


def to_unary(text):
    unary_text = ""
    prev_digit = False  # False = 0, True = 1
    # handle first character
    if len(text) >= 1:
        char = text[0]
        if char == "0":
            unary_text += "00 0"
        else:
            unary_text += "0 0"
            prev_digit = True

    for i in range(1, len(text)):
        char = text[i]
        if char == "0" and prev_digit:
            unary_text += " 00 0"  # switch from 1 to 0
            prev_digit = False
        elif char == "1" and not prev_digit:
            unary_text += " 0 0"  # switch from 0 to 1
            prev_digit = True
        else:
            unary_text += "0"  # repeat digit
    return unary_text


def main():
    text = raw_input()
    binary_text = to_binary(text)
    print >> sys.stderr, binary_text
    unary_text = to_unary(binary_text)
    print(unary_text)


if __name__ == "__main__":
    main()
