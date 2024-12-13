import math


def NULL_not_found(object: any) -> int:
    # your code her
    type_object = type(object)
    # print(type_object)
    if object is None:
        print(f"Nothing: {object} " + str(type_object))

    elif type_object is float and math.isnan(object):
        print(f"Chesse: {object} " + str(type_object))

    elif type_object is int and object == 0:
        print(f"Zero: {object} " + str(type_object))

    elif type_object is str and object == '':
        print(f"Empty: {object} " + str(type_object))

    elif type_object is bool and object is False:
        print(f"Fake: {object} " + str(type_object))

    else:
        print("Type not Found")
        return 1

    return 0
