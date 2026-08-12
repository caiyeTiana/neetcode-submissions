# NeetCode solution 2 - iteration (similar to video version)
# visualization很清楚

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        
        while list1 and list2: # 当两者都不为空时
            if list1.val < list2.val: # 或许list1.val指的是第一个值
                node.next = list1 
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next
