# NeetcodeVideo - Solution 2 Counter()

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)