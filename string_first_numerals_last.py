s=input('Enter the String:')
character=[]
integers=[]


for i in range(len(s)):
    if s[i].isalpha():
        character.append(s[i])
    else:
        integers.append(s[i])


res=sorted(character)+sorted(integers)


for j in res:
    print(''.join(j),end='')
print()


#input:a789bc34
#output:abc34789
        