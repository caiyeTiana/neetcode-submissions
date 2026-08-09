class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return any(a==b for a, b in pairwise(sorted(nums)))
        