import sys

def count_alpha(object: str) -> int:
    
    upper = 0
    lower = 0
    digit = 0
    spaces = 0
    punc = 0
    total = 0
    for letter in object:
        total += 1
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1
        elif letter.isspace():
            spaces += 1
        elif letter.isdigit():
            digit += 1
        else:
            punc += 1

    print(f"The text contains {total} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punc} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digit} digit")

    return 0
def main():

    len_arg = len(sys.argv)
    if len_arg == 1:
        return (print("you must provide a string"))
    try:
        assert len(sys.argv) == 2, "You must write only one string"
        arg = sys.argv[1]
        count_alpha(arg)
    except AssertionError as e:
        print(f"AssertionError : {e}")

    return 0

if __name__ == "__main__":
    main()
