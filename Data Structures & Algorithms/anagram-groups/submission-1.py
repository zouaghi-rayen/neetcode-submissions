from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
       
        for word in strs:
            sorted_word = tuple(sorted(word))
            
            anagram_map[sorted_word].append(word)
            
        # Return all the grouped lists
        return list(anagram_map.values())