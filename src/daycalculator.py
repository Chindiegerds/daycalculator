def is_leap(year):
    if year < 1500:
        return None
    if year%4==0 and year%100!=0:
        return True
    elif year%400==0:
        return True
    else:
        return False

def day_number_of_year(year, month, day):
    if year < 1500 or month < 1 or month > 12:
        return None
    days = {1 : 31, 2 : 29 if is_leap(year) else 28, 
            3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30,
            10 : 31, 11 : 30, 12 : 31 
            }
    if day < 1 or day > days[month]:
        return None
        
    number_of_days = 0;
    for m in range(1, month):
        number_of_days += days[m]
        
    return number_of_days + day


def main(): 
    status = True
    print("Day calculator")
    while status:
        try:
            x = 0
            while x != -1:
                year = int(input("enter year or -1 to quit: "))
                if year != -1:
                    month = int(input("enter month: "))
                    day = int(input("enter day: "))
                    days = day_number_of_year(year, month, day)
                    if days == None:
                        print("Invalid entry")
                    else:
                        print(f"day {days} of year {year}")
                x = year
                if year == -1:
                    status = False  
                    print("Thank you")
                print()
        except KeyboardInterrupt:
            print("\nYou selected to quit. Thank you!")
            x = -1
            break
        except Exception as e:
            print("Sorry an error occored Try again!")
        
if __name__ == "__main__":
    main()