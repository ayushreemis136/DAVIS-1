#create a list of 20 numbers and print the elements in backward direction using forward index
firstlist= [80,90,39,78,90,78,56,67,00,21,21,34,567,24,80,16,45,71,26,70]
print("the elements in the list are:   ")
print (" the elements in 4th element =  ",firstlist[2:10:2])
print("-------------------------")
x= len(firstlist)-1
for index in range(x,-1,-1):
    print(firstlist[index])
 

    
