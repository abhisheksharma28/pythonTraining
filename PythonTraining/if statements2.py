def max_num(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        print(str(num1)+" is max")
    elif num2>=num1 and num2>=num3:
        print(str(num2)+" is max")
    else:
        print(str(num3)+" is max")

max_num(300,4,50)
