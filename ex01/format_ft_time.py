# Allowed functions : time, datetime or any other library that allows to
# receive the date

#output:

#Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
#Oct 21 2022$

from datetime import datetime
import time
from decimal import Decimal

def get_today_date():
    dt = datetime.today()
    year = dt.year
    day = dt.day
    month = dt.strftime("%B")

    date = month + " " + str(day) + " " + str(year)
    print(date)


def science_format(nb) -> str:
    stree =  f"{Decimal(nb):.2e}"

    return str(stree)

def show_time_of_the_day():
    txt = "Seconds since January 1, 1970: "

    # format second with comas
    time_now = time.time()
    second = round (time_now, 4)
    second = f'{second:,}' 

    #convert scientific format
    science_f = science_format(time_now)

    txt = txt + str(second) + " or " + science_f + " in scientific notation"
    print(txt)

    get_today_date()

def main():
    show_time_of_the_day()

if __name__  == '__main__':
    main()