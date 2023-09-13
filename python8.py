#input:a4b3c2
#output:aaaabbbcc




s=input("Enter the string:")
output=""



for i in range(len(s)):
    if s[i].isalpha():
        var=s[i]
    else:
        num=int(s[i])
        output=output+(var*num)



print(outputa)