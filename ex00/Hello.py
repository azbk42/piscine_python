ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here
#list
ft_list[1] = "World!"

#tuple
ft_tuple = list(ft_tuple)
ft_tuple[1] = "France!"
ft_tuple = tuple(ft_tuple)

#set
ft_set.remove("tutu!")
ft_set.add("Paris!")


#dict
ft_dict["Hello"] = "42Paris"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)