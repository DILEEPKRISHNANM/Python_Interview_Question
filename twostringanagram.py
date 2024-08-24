def isAnagram(s1,s2):
    return sorted(s1) == sorted(s2)


str1 =input("\n Enter the String:")
str2 = input("\n ENter the second string :")


answer = isAnagram(str1,str2)

if answer:
    print("Yes it is a angram")

else:
    prit("No it is an anagram")