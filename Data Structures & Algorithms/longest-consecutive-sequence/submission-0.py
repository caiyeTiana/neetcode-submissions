# NeetCode solution3 - hash table
# length = 0的video version其实差不多，只不过length = 1少跑一次循环

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)  
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1 # video version 这里是0， 但结果一样
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest