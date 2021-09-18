while True:
    year= input("Enter Year: ")
    if year.capitalize()=="Exit":
        break
    elif year.capitalize()!="exit" and  year.isnumeric()==False:
        print("Invalid Entry.Year entered is either less than zero or is not numeric,Kindly enter a new year or type exit to quit")
    
    
    else:
        year=int(year)
        if year<0:
         print("The year",year,"is not a valid year") 
        elif year%4!=0:
            print("The Year",year,"is a normal year")
            
        elif year%100==0:
            if year%400==0:
                print("The Year",year,"is a leap year")
            else:
                print("The Year",year,"is a normal year")
        else:
           print("The Year",year,"is a leap year")
    
