#chocolate packing:

Chocolate_packets=[]
packet=input("Enter the values of each packets:")
Chocolate_packets=list(map(int,packet.split()))
print("The chocolate packets are:",Chocolate_packets)
Packed_packets=[]
Empty_packets=[]
for i in Chocolate_packets:
    if(i==0):
        Empty_packets.append(i)
    else:
        Chocolate_packets.append(i)
arr_sort=sorted(Chocolate_packets)
Final_arrangement=arr_sort+Empty_packets
print("The Final_arrangement is:",Final_arrangement)

    
    
    

