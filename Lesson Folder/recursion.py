def timer(num):
    if num <= 0:
        print("Addictive Python")
    else:
        print(num)
        timer(num-1)
print(timer(10))
