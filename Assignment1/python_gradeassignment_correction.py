
while True:

    input_value = input("Enter Exams score: ")
    
    if input_value.capitalize() == 'Exit':
        break
    
    elif input_value.capitalize() != "Exit" and input_value.isnumeric() == False:
        print("Invalid Entry")
    
    else:
        score = float(input_value)
    
        if score >= 90 and score <= 100:
            print("Student wins a laptop")

        elif score >= 60 and score < 90:
            print("Student wins a Tablet")
    
        elif score < 60 and score >= 0:
            print("Student wins nothing")  
        
        else:
            print("Invalid score entered,kindly enter a valid score between 0 and 100")    
    
    
