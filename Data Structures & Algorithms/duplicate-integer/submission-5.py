# Hash Set - NeetCode
# Q: 对于hash table solution,为什么左侧的示意图中，seen set里，1对应的是true, 2对应的也是true？明明1和2并没有重复 #A: 三行都是 true，只是说明这三个数都被存过。真正触发返回的是第 4 个 num 查到了已存在的 3
# Q: 那对这个例子，最终返回的那一个True,和seen里的三个true是什么关系？ A: 没关系，同名不同物。那些 true 是可视化工具自己画上去的占位符。

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False