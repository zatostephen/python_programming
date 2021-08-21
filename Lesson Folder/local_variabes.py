x = 50
print("x is",x)
def func(x):
	print("x is", x)

x= 2
print("Changed Global x to ", x)
func(x)
print("x is still" , x)
func(20)
print("x is still", x)