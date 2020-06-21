#URL: https://leetcode.com/problems/linked-list-cycle/
#Given a linked list, determine if it has a cycle in it.
#To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed)
#in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
#Example 1:
#Input: head = [3,2,0,-4], pos = 1
#Output: true
#Explanation: There is a cycle in the linked list, where tail connects to the second node.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Hash Map approach - O(N) space and O(N) time
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        myHash = dict()
        while head:
            if head not in myHash:
                myHash[head] = None
            else:
                return True
            head = head.next
        return False

# Slow/Fast Pointers Approach - O(N) time and 0(1) space
    def hasCycle2(self, head: ListNode) -> bool:
        if not head:
            return False

        slow = head
        fast = head.next

        while slow and fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next

        return False
