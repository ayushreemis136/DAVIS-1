print( " the numbers between 100 and 1000 which are even and divisible by 3 are :  ")
count = 0
for x in range (100,1000):
     if ( x%3==0 and x%2==0):
       print(x ,end=' , ')
count+=1
print (" Total No. =   ",count)
         
         
