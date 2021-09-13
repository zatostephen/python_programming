
#A leap year containing an extra day. It has 366 days instead of the normal 365 days.
#The extra day is added in February, which has 29 days instead of the normal 28 days.
#Leap years occur every 4 years. 2020 is a leap year and so is 2024.
#Except that every 100 years special rules apply. For example 1900 was not a leap year, but 2000 was.

while True:
    
    year=input("Enter Year:")

    if year.capitalize()=="Exit":
        break
    elif year.capitalize!="exit" and year.isnumeric()==False:
        print("Invalid Entry,kindly enter a valid year")
    else:
        year=int(year)
        if year%4!=0:
           print(year,"is a normal year")
        elif year%100==0:
            if year%400==0:
                print(year,"is a leap year")
            else:
                print(year,"Normal year")
        
        else:
            print(year,"is a leap year")
