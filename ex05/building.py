import sys


def count_alpha(text: str) -> int:
    """
    Counts the types of characters in a string and prints a summary.

    Args:
        text (str): The string to analyze.

    Returns:
        int: Always returns 0.
    """
    upper = 0
    lower = 0
    digit = 0
    spaces = 0
    punc = 0
    total = 0

    for letter in text:
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
    """
    Main function to handle command-line argument and call count_alpha.
    """
    if len(sys.argv) == 1:
        print("you must provide a string")
        return 0
    try:
        assert len(sys.argv) == 2, "You must write only one string"
        arg = sys.argv[1]
        count_alpha(arg)
    except AssertionError as e:
        print(f"AssertionError: {e}")
    return 0


if __name__ == "__main__":
    main()
