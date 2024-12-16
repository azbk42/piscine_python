from collections import Counter

import sys
import string


def building_function(str1: str):
    """
    Analyzes the content of a string and displays statistics
    on the number of uppercase letters, lowercase letters,
    digits, punctuation marks, and spaces.

    Args:
        str1 (str): The string to be analyzed.
    """

    table = Counter(str1)
    total = sum(table.values())
    digit = sum(1 for letter in table if letter.isdigit())
    up = sum(1 for letter in table if letter.isupper())
    low = sum(1 for letter in table if letter.islower())
    nb_punct = sum(1 for letter in table if letter in string.punctuation)
    space = table[" "]

    print(f"The text contains {total} characters:")
    print(f"{up} upper letters")
    print(f"{low} lower letters")
    print(f"{nb_punct} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def check_errors(args: list):
    """
    Checks that the number of arguments passed to the script is correct.

    Args:
        args (list): The list of arguments passed via the command line.

    Raises:
        AssertionError: If more than one argument is provided to the script.
    """
    if len(args) > 2:
        raise AssertionError("You must only write one string or nothing")


def main():
    """
    Main entry point of the script.

    Functionality:
    - If no arguments are provided, the user is prompted to enter a text
      via the console.
    - If one argument is provided, that argument is analyzed directly.
    - If more than one argument is provided, an AssertionError is raised.

    The text is then analyzed by the `building_function` to display
    statistics about its content.

    Raises:
        AssertionError: If more than one argument is provided to the script.
    """
    try:
        # Check if the correct number of arguments is provided
        check_errors(sys.argv)
        if len(sys.argv) == 1:
            prompt = input("What is the text to count?\n")
            building_function(prompt)
        else:  # If one argument is provided, analyze it
            building_function(sys.argv[1])
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Unexpected Error ({type(e).__name__}): {e}")


if __name__ == "__main__":
    """
    Main entry point of the script.
    """
    main()
