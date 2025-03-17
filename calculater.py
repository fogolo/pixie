def add(x ,y):
    return x+y
def minose(x,y):
    return x-y
def multy(x,y):
    return x*y
def devide(x,y):
    return x/y
print("the subject will start now please select what type u want")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.devide")
choices=input("put nember_from 1 to 4:")
if choices=='1' or '2' or '3' or '4':
    num1=float(input("write ur number here:"))
    num2=float(input("write ur number here:"))
    if choices =="1":
        print("Result:", add(num1, num2))
    elif choices == '2':
        print("Result:", minose(num1, num2))
    elif choices == '3':
        print("Result:", multy(num1, num2))
    elif choices == '4':
        if num2 != 0:
            print("Result:", devide(num1, num2))
        else:
            print("Cannot divide by zero!")    
    else:
            print("ur wrong man try the option")
