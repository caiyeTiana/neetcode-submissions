# NeetcodeVideo - Solution 3 sorted()

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)