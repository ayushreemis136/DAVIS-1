cp=float(input("enter the cost price=  "))
sp=float(input(" enter the selling price= "))

if(cp < 0):
    print(" cost price is invalid ")
elif(sp < 0):
    print(" invalid selling price ")
else:
    #determining loss and profit
    if(sp>cp):
     print( " profit : "( sp-cp))
    elif(cp>sp):
     print(" loss : "( cp-sp))
    else:
     print( " no profit no loss ")






















































