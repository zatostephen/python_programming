# R: F = G(m1m2)/R2
#create variables that request an expected input from the user.ie input for m1,m2 and r.
m1=float(input("Enter mass of first object: "))
m2=float(input("Enter mass of second object: "))
r=float(input("Enter Distance between the objects: "))
#create variable that calculate the numerator part of the formula(G*m1*m2)
numerator= (6.67*10**-11)*m1 * m2
#create variables that calculate the denomenator of the formula
denominator=r**2
#create a function that calculate numerator/denomenator
fg=numerator/denominator
#print function to display the output
print("Fg= ",fg,"N or Newthon")
#create variables that stores input received from users
m1=input()
m2=input()
r=input()
         

