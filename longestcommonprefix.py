def prefixprint(string_list):
    if len(string_list)==0:
        return ""
    else:
        prefix=string_list[0]
        for i in string_list[1:]:
            while not i.startswith(prefix):
                prefix=prefix[:-1]
                if not prefix:
                    return ""
        return prefix


string_list=eval(input("enter the list"))
print(prefixprint(string_list))



#enter the list["flower","flow","flee"]
#fl