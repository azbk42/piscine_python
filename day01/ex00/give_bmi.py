import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[float]:
    """
    Calculates the Body Mass Index (BMI) for a list of heights and weights.

    **Parameters**
    ----------
    height : list[int | float]
        List of heights in meters.
    weight : list[int | float]
        List of weights in kilograms.

    **Returns**
    -------
    list[float]
        List of BMI values for each (height, weight) pair.

    **Raises**
    -------
    ValueError
        If `height` and `weight` do not have the same length.
    TypeError
        If any element in `height` or `weight` is not an int or float.

    **Example**
    -------
    >>> give_bmi([1.75, 1.8], [70, 80])
    [22.86, 24.69]
    """
    if len(height) != len(weight):
        raise ValueError("Argument error, different length")
    for x, y in zip(height, weight):
        if not isinstance(x, (int, float)):
            raise TypeError(f"Bad type height: {x}")
        if not isinstance(y, (int, float)):
            raise TypeError(f"Bad type weight: {y}")

    h_np = np.array(height)
    w_np = np.array(weight)

    bmi_tab = w_np / (h_np * h_np)
    return bmi_tab.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Checks if BMI values exceed a given limit.

    **Parameters**
    ----------
    bmi : list[int | float]
        List of BMI values.
    limit : int
        The limit to be applied.

    **Returns**
    -------
    list[bool]
        List of booleans where True means BMI > limit.

    **Raises**
    -------
    TypeError
        If any element in `bmi` is not an int or float.

    **Example**
    -------
    >>> apply_limit([22.5, 24.8, 30.1], 25)
    [False, False, True]
    """
    bmi_np = np.array(bmi)
    if not np.issubdtype(bmi_np.dtype, np.number):
        raise TypeError(f"Bad type bmi")
    condition = bmi_np > limit
    return condition.tolist()


def main():
    """
    Main function to execute BMI calculation and apply a limit.

    **Workflow**
    ------------
    1. Calculates BMI for a list of heights and weights.
    2. Applies a limit to the BMI values.
    3. Prints the results.

    **Exceptions Handled**
    ---------------------
    - ValueError: If input heights and weights have different lengths.
    - TypeError: If input types are incorrect.
    - Generic Exception: Handles any other unexpected errors.

    **Example**
    -------
    >>> main()
    [22.86, 29.06]
    [False, True]
    """
    try:
        height = [-5, 1.15]
        weight = [165.3, 38.4]

        bmi = give_bmi(height, weight)
        print(bmi)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except ValueError as e:
        print(f"ValueError: {e}")
    except TypeError as e:
        print(f"TypeError: {e}")
    except Exception:
        print("Error")


if __name__ == '__main__':
    main()
