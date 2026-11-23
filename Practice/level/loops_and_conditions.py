a = int(input("Enter a number: "))

if a > 0:
    print("it is positive number")
    if a%2 == 0:
        print("it is even number")
    else: 
        print("it is odd number")
elif a < 0:
    print("it is negative number")
else:
    print("it is zero")