def NULL_not_found(object: any) -> int:

    type_object = type(object)

    if type_object == type(None):
        print(f"Nothing: {object} {type_object}")
    elif type_object == float and str(object) == "nan":
        print(f"Cheese: {object} {type_object}")
    elif type_object == int and object == 0:
        print(f"Zero: {object} {type_object}")
    elif type_object == str and object == "":
        print(f"Empty: {object} {type_object}")
    elif type_object == bool and object is False:
        print(f"Fake: {object} {type_object}")
    else:
        print("Type not Found")
        return 1
    return 0


'''
$>python tester.py | cat -e
Nothing: None <class 'NoneType'>$
Cheese: nan <class 'float'>$
Zero: 0 <class 'int'>$
Empty: <class 'str'>$
Fake: False <class 'bool'>$
Type not Found$
1$
$>
'''