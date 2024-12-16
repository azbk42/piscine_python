import sys


def check_arg(argv: list):
    if len(argv) == 1:
        return
    elif len(argv) > 2:
        raise AssertionError("more than one argument is provided")
    try:
        x = int(argv[1])
        if x % 2 == 0:
            return print("I'm Even")
        else:
            return print("I'm Odd")
    except ValueError:
        raise AssertionError("argument is not an integer")


def main():
    try:
        check_arg(sys.argv)
    except AssertionError as e:
        print(f"AssertionError: {e}    ")


if __name__ == '__main__':
    main()
