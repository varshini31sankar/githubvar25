def add(x,y):
    return x+y

def subract(x,y):
    return x-y

def multiply(x,y):
    return x*y
    

def divide(x,y):
    return x/y

   
print("select the operation")
print("1 add")
print("2 subract")
print("3 multiply")
print("4 divide")

while True:
    choice = input("Enter Choice (1/2/3/4: ")
    if choice in("1","2","3","4"):
        num1= float(input("Enter first Number : "))
        num2= float(input("Enter second Number : "))
        if choice =='1':
            print(num1,"+",num2,"=", add(num1,num2))
            
        elif choice =="2":
             print(num1,"-",num2,"=", subract(num1,num2))
        elif choice =="3":
             print(num1,"*",num2,"=", multiply(num1,num2))
        elif choice =="4":
             print(num1,"/",num2,"=", divide(num1,num2))
             break
             Else:print("invalid")
       
            
    



    


