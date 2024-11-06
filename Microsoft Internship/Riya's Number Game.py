#riya's number game
Array1=[]
numbers=input("Enter some numbers spearated by spaces:")
Array1=list(map(int,numbers.split()))
print("your array is :",Array1)
sorted_array=Array1.sort(reverse=True)
print(sorted_array)
