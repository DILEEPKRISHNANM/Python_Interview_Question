# from collections import defaultdict

# def groupanagram(strs):
#     anagrams = defaultdict(list)

#     for s in strs:
#         key= tuple(sorted(s))
#         anagrams[key].append(s)

#     for value in anagrams.values():
#         print(value)




# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# groupanagram(strs)

from collections import defaultdict
def anagram(strs):
    anagrams = defaultdict(list)

    for s in strs:
        key  = tuple(sorted(s))
        anagrams[key].append(s)


    for i in anagrams.values():
        print(i,end=" ,")
    print()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagram(strs)