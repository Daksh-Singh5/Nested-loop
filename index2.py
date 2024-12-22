num1 = int(input("Enter your Number of rows: "))
num2 = int(input("Enter your Number of column: "))


for i in range(num1):
    for j in range(num2):
        print(i ,j,end=" | ")
    print("")