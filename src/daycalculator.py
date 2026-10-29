def is_leap(year):
    if year < 1500:
        return None
    if year%4==0 and year%100!=0:
        return True
    elif year%400==0:
        return True
    else:
        return False

def days_in_month(year, month):
    if year < 1500 and month < 0 or month > 12:
        return None
    if month==1 or month==3 or month==5 or month==7 or month == 8 or month==10 or month==12:
        return 31
    elif month==2:
        if is_leap(year):
            return 29
        else:
            return 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30

def day_number_in_year(year, month, day):
    if year < 1500 and month < 0 or month > 12:
        return None
    if month == 1:
        return day
    elif month == 2:
        if is_leap(year):
            return days_in_month(year, month) + day
        else:
            return days_in_month(year, month) + day
    elif month == 3:
        if is_leap(year):
            return 60 + day
        else:
            return 59 + day
    elif month == 4:
        if is_leap(year):
            return 91 + day
        else:
            return 90 + day
    elif month == 5:
        if is_leap(year):
            return 121 + day
        else:
            return 120 + day
    elif month == 6:
        if is_leap(year):
            return 152 + day
        else:
            return 151 + day
    elif month == 7:
        if is_leap(year):
            return 183 + day
        else:
            return 182 + day
    elif month == 8:
        if is_leap(year):
            return 214 + day
        else:
            return 213 + day
    elif month == 9:
        if is_leap(year):
            return 244 + day
        else:
            return 243 + day
    elif month == 10:
        if is_leap(year):
            return 274 + day
        else:
            return 273 + day
    elif month == 11:
        if is_leap(year):
            return 304 + day
        else:
            return 303 + day
    elif month == 12:
        if is_leap(year):
            return 335 + day
        else:
            return 334 + day



active = True
print("Day calculator")
while active:
    day, month, year = int(input("Enter the date or -1 to quit: ")), 0, 0
    if day != -1:
        month = int(input("Enter the month: "))
        year = int(input("Enter the year: "))

    if day == -1:
        active = False
        print("Thank you")
    else:
        day_number = day_number_in_year(year, month, day)
        if is_leap(year):
            print(f"Day {day_number} of 366 in year {year}")
        else:
            print(f"Day {day_number} of 365 in year {year}")

