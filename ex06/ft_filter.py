

def ft_filter(func, iterable) -> filter:
    '''filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    '''
    if func is None:
        return [x for x in iterable if x]
    return [x for x in iterable if func(x)]

# help(filter)
# print(ft_filter.__doc__)


# def long_word(x):
#     return len(x) > 3


# def main():

#     list_test = ["salut", "bonjour", "yo", "ah", "BonSoirrr", "888888"]

#     result = ft_filter(long_word, list_test)
#     print(result)

#     numbers = [-3, 0, 4, 7, -1, 2]

#     result = ft_filter(lambda n: n % 2 == 0, numbers)
#     print(result)
#     return 0


# if __name__ == "__main__":
#     main()
