class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = collections.Counter(s)
        dict_t = collections.Counter(t)
        
        return dict_s == dict_t
        
=================================================================

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        
        for item in s:
            dict_s[item] = dict_s.get(item, 0) + 1
        for item in t:
            dict_t[item] = dict_t.get(item, 0) + 1
        
        return dict_s == dict_t
