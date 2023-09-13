str1=input("enter the string:")




c=int(input("enter the count:"))


str1=str1.split()
dict={}
res=[]

#print(str1)


for i in str1:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1


for key in dict:
    if dict[key] >=c:
        res.append(key)



if len(res)>0:
    print(res)

else:
    print("NA")


#words occuring number of times give in the input
#input:man dk dk dk dk dk ct
#      :2
#output:dk  

