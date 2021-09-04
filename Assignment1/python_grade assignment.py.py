#we create a variable to store exams score from user
score=float(input("Enter Exams score: "))
# we create condition number 1 (scores bet 90 and 100
if score >=90 and score <=100:
#we print if condition one is met
    print("Student wins a laptop")

#we use elif function for the second condition.That is if score falls bet 60 and 90 
elif score >=60 and score <90:
#we print if second condition is met
    print("Student wins a Tablet")
# we use elif function for the third condition
elif score < 60 and score >=0:
#we print if third condition is met
      print("Student wins nothing")
# We use else function to print an out to prompt user of an invalid entry
else:
    print("Invalid score entered,kindly enter a valid score between 0 and 100")

     
    
    
