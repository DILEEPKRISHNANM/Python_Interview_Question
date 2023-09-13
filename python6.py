#input
#n=5,s='abcde',m=4,t=['abcd','acde','acbc']



def stringc(n,s,m,t):
    count=0


    x=[]
    for i in s:
        x.append(i)

    print(x)

    for char in range(n):
        ch=x.pop(char)
        if ''.join(x) in t:
            count+=1
        x.insert(char,ch)

    print(count)


stringc(5,'abcde',4,['abcd','acde','cabc'])