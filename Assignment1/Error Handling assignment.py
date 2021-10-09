
while True:
        def  di_two_numbers(number_1,number_2):
                number_1=float(input("Enter first number: "))
                number_2=float(input("Enter second number: "))
                if number_2==0:
                        print("Invalid number entered,Kindly enter a valid integer number")
                else:
                        return number_1/number_2
        print(di_two_numbers(10,2))
