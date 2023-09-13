# input:dileep
# output:e


#maximum occuring character in a string




s=input("enter the string")


res=0
dict={}

word=s.replace(' ','').lower()


for i in word:
    if i.isalpha():
        dict[i]=dict.get(i,0)+1
    

    else:
        pass




res=max(dict,key=dict.get)


print(res)