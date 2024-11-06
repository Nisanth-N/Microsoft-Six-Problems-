list=[1,2,3,4,3,6,2]
count=0
for i in range(1,len(list)):
  if(list[i]%2!=0):
    count=count+1
print("The No. of times the green pen is switched to red pen is:", count)


