# def isAnagram(a, b):
#     if len(a) != len(b):
#         return False
    
#     count = {}

#     # count characters in a
#     for ch in a:
#         count[ch] = count.get(ch, 0) + 1

#     # subtract using b
#     for ch in b:
#         if ch not in count:
#             return False
#         count[ch] -= 1
#         if count[ch] < 0:
#             return False

#     return True


# def groupAnagrams(strs):
#     n = len(strs)
#     visited = [False] * n
#     result = []

#     for i in range(n):
#         if visited[i]:
#             continue

#         group = [strs[i]]
#         visited[i] = True

#         # compare strs[i] with all remaining words
#         for j in range(i + 1, n):
#             if not visited[j] and isAnagram(strs[i], strs[j]):
#                 group.append(strs[j])
#                 visited[j] = True

#         result.append(group)

#     return result


def groupAnagrams(strs):
    groups = {}  

    for word in strs:
        key = "".join(sorted(word))   

        if key not in groups:
            groups[key] = []        

        groups[key].append(word)      

    return list(groups.values())       

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))