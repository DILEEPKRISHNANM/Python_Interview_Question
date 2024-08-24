s=input("Enter The String:")
dict1={}
for i in s:
    dict1[i] = dict1.get(i,0)+1


minval = min(dict1,key=dict1.get)

for key,value in dict1.items():
    if value == 1:
        print(key)
        break