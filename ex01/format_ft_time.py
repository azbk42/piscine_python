from datetime import datetime



date = datetime.now()
time = date.timestamp()

final_number = round(time, 4)
res = "{:,}".format(final_number)

print('Seconds since January 1, 1970: ', end="")

print(res, end="")
print(" or ", end="")

print(f"{final_number:.2e}", end="")
print(" in scientific notation")

print(date.strftime("%b %d %Y"))

#print(dir(date))
#help(date)
#help(date.strftime)
#Allowed functions: time, datetime or any other library that allows to receive the date

#output
'''
$>python format_ft_time.py | cat -e
Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
Oct 21 2022$
'''