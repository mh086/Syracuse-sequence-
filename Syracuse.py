def Syracuse(num): #"num" is equal to number
    if (num % 2 ==0):
        return num // 2
    elif (num % 2 == 1):
        return num*3+1
    else:
        print("Something is wrong with the Syracuse Sequence")
        return None
print ("Please Enter a Natural Number to get the Syracuse Sequence:")
num = int(input())
print("he Syracuse Sequence Numbers are:")
print(num)
while(num!=1):
    num = Syracuse(num)
    print(num)