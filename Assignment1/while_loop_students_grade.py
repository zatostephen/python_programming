

score=" "

while score !="exit":
    # break is not working,displays"ValueError: could not convert string to float: 'exit'" trying to resvove it
    score=float(input("Enter Exams score: "))
    if score >=90 and score <=100:
        print("Student wins a laptop")
    elif score >=60 and score <90:
        print("Student wins a Tablet")
    elif score < 60 and score >=0:
          print("Student wins nothing")
    else:
        print("Invalid score entered,kindly enter a valid score between 0 and 100")

     
    
    
