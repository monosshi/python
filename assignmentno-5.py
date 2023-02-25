# MONOSSHI ZAMAN
# ID-0182210012101147

num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
remainder1= num1 % 5
print(remainder1)
remainder2= num2 % 5
print(remainder2)
if(remainder1 and remainder2 % 2==0):
    print("Even")
else:
    print("Odd")
    