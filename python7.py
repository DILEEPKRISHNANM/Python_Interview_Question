
def visting(lis,a,b):
    if a<0 or a>=b:
        return
    else:
        print(lis[a],end=' ')
        visting(lis,a+1,b)
    
    


lis=eval(input("Enter the array:"))

a=int(input("Enter the Rabge:"))

b=int((input("Enter the Range")))


visting(lis,a,b)



#traversing elements in an array without using loop



