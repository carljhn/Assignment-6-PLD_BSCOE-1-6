#Number Sorter
#Create a program that ask 4 numbers. 
#Print the 4 numbers from highest to lowest using only if-else statement.
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
num4=int(input("Enter fourth number: "))

if num1>=num2 and num1>=num3 and num1>num4:
    if num2>=num3 and num2>num4:
        if num3>=num4:
            print(num1, num2, num3, num4)
        else:
            print(num1, num2, num4, num3)
    else: 
        if num3>=num2 and num3>num4:
            if num2>=num4:
                print(num1, num3, num2, num4)
            else: #num4>num2
                print(num1, num3, num4, num2)
        else: 
            if num4>num3:
                if num2>num3:
                    print(num1, num4, num2, num3)
                else: #num3>num2
                    print(num1, num4, num3, num2)

else:
    if num2>=num1 and num2>num3 and num2>=num4:
        if num1>=num3 and num1>num4:
            if num3>=num4:
                print(num2, num1, num3, num4)
            else: #num4>num3   
                print(num2, num1, num4, num3)
        else: #num3>num1
            if num3>=num1 and num3>num4:
                if num1>=num4:
                    print(num2, num3, num1, num4)
                else: #num4>num1
                    print(num2, num3, num4, num1)
            else:
                if num4>=num3:
                    if num3>=num1:
                        print(num2, num4, num3, num1)
                    else: #num1>num3
                        print(num2, num4, num1, num3)
    else: 
        if num3>=num2 and num3>=num1 and num3>=num4: 
            if num1>=num2 and num1>num4:
                if num2>=num4:
                    print(num3, num1, num2, num4)
                else: #num4>num2
                    print(num3, num1, num4, num2)
            else:
                if num2>num1 and num2>=num4:
                    if num4>=num1:
                        print(num3, num2, num4, num1)
                    else: #num1>=num4
                        print(num3, num2, num1, num4)
                else:
                    if num1>=num2:  
                        print(num3, num4, num1, num2)
                    else:
                        print(num3, num4, num2, num1)
