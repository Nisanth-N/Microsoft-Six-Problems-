print("Menu Card:")
print("Pizza - 200")
print("Burger - 130")
print("Briyani - 250")
print("Dosa - 80 ")
print("Idly - 50")

i=int(input("No.of Pizzas ordered:"))
j=int(input("No.of Burger ordered:"))
k=int(input("No.of Briyani ordered:"))
l=int(input("No.of Dosa ordered:"))
m=int(input("No.of Idly ordered:"))
quantity= i+j+k+l+m
print("quantity=",quantity)
total_sum=(i*200+j*130+k*250+l*80+m*50)
print("total_sum",total_sum)

if (total_sum>600):
    print(total_sum-((10/100)*total_sum))
else:
    print(total_sum)

