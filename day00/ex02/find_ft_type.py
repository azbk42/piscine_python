def all_thing_is_obj(object: any) -> int:
    type_object = type(object)

    if type_object is list:
        print("List : " + str(type_object))
    elif type_object is tuple:
        print("Tuple : " + str(type_object))
    elif type_object is set:
        print("Set : " + str(type_object))
    elif type_object is dict:
        print("Dict : " + str(type_object))
    elif type_object is str:
        print(f'{object}  is in the kitchen : ' + str(type_object))
    else:
        print("Type not found")

    return 42
