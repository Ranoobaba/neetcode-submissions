from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we have group of strings, what we want to return is a list with a subgroup of strings that are assigned via if they are anagrams of each other.
        #my intution here is telling me that we have to do some anagram logic, then group them and store them via a hashmap that is a list then return list of that hashmapvalues?
        #lets have a anagram function I can remeber kinda how to use the anagram code make a small class, call that for each word then if its an anagram add it to the sorted key value. I can sort the first value i get that is not in the hashmap already
        #return the hashmap.values and then slam it into a list?
        anagram_store = defaultdict(list)
        for word in strs:
            list_of_letters = sorted(word)
            seperator = ''
            sorted_wholeword = seperator.join(list_of_letters)
            anagram_store[sorted_wholeword].append(word)
        return list(anagram_store.values())

        