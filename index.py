num1 = int(input("Enter your Number to start with: "))
num2 = int(input("Enter your Number to end with: "))

for i in range(num1,num2+1,1):
    flag = True
    for div in range(2,i,1):
        if(i%div==0):
            flag=False
            break
    if(flag):
       print(i,end=" ")
