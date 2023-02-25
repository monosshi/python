# MONOSSHI ZAMAN
# ID-0182210012101147

num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
num3=int(input("Enter a number:"))
if num1>num2 and num1>num3:
    if num2>num3:
        print("{} is the second largest number".format(num2))
    else:
        print("{} is the second largest number".format(num3))
elif num2>num3 and num2>num1:
    if num1>num3:
        print("{} is the second largest number".format(num1))
    else:
        print("{} is the second largest number".format(num3))
else:
    if num1>num2:
        print("{} is the second largest number".format(num1))
    else:
        print("{} is the second largest number".format(num2))
        