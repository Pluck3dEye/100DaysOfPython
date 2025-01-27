def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        month_days[1] = 29
        return month_days[month-1]
    else:
        return month_days[month-1]


year = int(input("Year: "))
month = int(input("Month: "))
number_of_days_in_month = days_in_month(year, month)
print(number_of_days_in_month)

