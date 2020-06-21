#URL: https://leetcode.com/problems/merge-two-sorted-lists/
#Merge two sorted linked lists and return it as a new sorted list.
#The new list should be made by splicing together the nodes of the first two lists.

#temp: 1->1->2->3->4->4
# Edge case: l1: empty, l2: non-empty --> Return l2
# Edge case: l1: non-empty, l2: empty --> Return l1
# Edge case: l1 and l2: empty --> Return None
# Happy case: l1, l2 non-empty but have different lengths: 1->2->4->8, 1->2->3 --> Return 1->1->2->2->3->4->8->Null
# Happy case: l1: 1->Null, l2: 1->Null --> Return 1->1->Null

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Example:
#Input: 1->2->4, 1->3->4
#Output: 1->1->2->3->4->4
#l1: 1              ->              2               ->              4               ->               Null
#    new_head                       cur                             l1
#l2: 1              ->              3               ->              4               ->               Null
#                                   l2
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Edge cases when either l1 or l2 is empty
        if not l1:
            return l2
        if not l2:
            return l1

        if l1 and l2:
            if l1.val <= l2.val:
                cur = l1
                l1 = l1.next
            else:
                cur = l2
                l2 = l2.next
            new_head = cur

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                cur = l1         # very important step: needs to update position of cur to move through list
                l1 = l1.next
            else:
                cur.next = l2
                cur = l2
                l2 = l2.next

        if not l1:
            cur.next = l2
        if not l2:
            cur.next = l1

        return new_head
