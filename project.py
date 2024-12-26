Num = input("Enter your number: ")
i = 0
ans = 0
single=0
answer = 0
Numcopy = int(Num)
while Numcopy > 0:
    ans = ans*10+Numcopy%2
    Numcopy//=2
while ans>0:
    single = ans%10
    answer=(answer*10)+single
    ans = ans//10
print(answer)