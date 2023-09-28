def arrayrotation(li,k):
    for i in range(k):
        a=li.pop()
        li.insert(0,a)

    print(li)




li=[2,3,4,5,7,8]


k=int(input("\nEnter The Rotation:"))

arrayrotation(li,k)

