

def all_thing_is_obj(object: any) -> int:

    type_object = type(object)
    flag = True

    if type_object == str:
        print(f'{object} is in the kitchen : ', end="")
    elif type_object == list:
        print("List : ", end="")
    elif type_object == tuple:
        print("Tuple : ", end="")
    elif type_object == set:
        print("Set : ", end="")
    elif type_object == dict:
        print("Dict : ", end="")
    else:
        print("Type not found")
        flag = False
    
    if flag == True:
        print(type_object)
    return 42

'''
$>python tester.py | cat -e
List : <class 'list'>$
Tuple : <class 'tuple'>$
Set : <class 'set'>$
Dict : <class 'dict'>$
Brian is in the kitchen : <class 'str'>$
Toto is in the kitchen : <class 'str'>$
Type not found$
42$
$>
'''