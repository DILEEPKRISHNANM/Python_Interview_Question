s=int(input("enter the value:"))



s=bin(s)


print(s)


s=s[2:]
print(s)
t=''
sum=0


for i in s:
    if i=='0':
        t=t+'1'
    elif i=='1':
        t=t+'0'



x=len(t)

for j in range(0,x):
    sum += int(t[j])*(2**(x-(j+1)))



print(sum)
