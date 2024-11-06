m=int(input("Enter a Number:"))
n=int(input("Enter a Number:"))
sum=0
if m>n:
    print("0") 
else:
    for i in range(m,n+1):
        sum=sum+(i**3);
print(sum)

