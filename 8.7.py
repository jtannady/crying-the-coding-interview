# 8.7 Permutations with Dups
# Write a method to compute all permutations of a string of unique characters

def dups(string):
    # Base case
    if (len(string) == 1):
        return [string]
        
    array = []
    for char in string: # for a, for b, for c 
        sublist_perm = dups(string.replace(char, '')) # for a: ["bc", "cb"], for b: ["ac", "ca"], for c: ["ab", "ba"]
        for word in sublist_perm: 
            array.append(char + word)
    return array

print dups("a")
print dups("ab")
print dups("abcd")
#print dups("abcdefg")