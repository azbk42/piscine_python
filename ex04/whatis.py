import sys

arg = sys.argv[1:]

if arg:
    try:
        assert len(arg) == 1, "more than one argument is provided"

        number = int(arg[0])
        assert type(number) == int, "argument is not an integer"

        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except ValueError:
        print("AssertionError: argument is not an integer")
