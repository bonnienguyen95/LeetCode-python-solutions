#URL: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
#Given a sorted linked list, delete all duplicates such that each element appear only once.

#Input: 1->1->2->Null
#Output: 1->2->Null

#Test case 1: Input: Null --> Output: Null
#Test case 2: Input: 1 --> Output: 1
#Test case 3: Input: 1->1->1 --> Output: 1
#Test case 4: Input: 1->1->2->Null --> Output: 1->2->Null

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Check whether list is empty
        if head:
            cur = head
            nextNode = cur.next  # Establish next node after head
        else:
            return None

        # If list has more than 1 element, start loop. If not, loop will not start, return head
        while nextNode:
            if cur.val == nextNode.val:
                cur.next = nextNode.next
            else:
                cur = nextNode
            nextNode = nextNode.next  # reset nextNode

        return head

# O(n) time and O(1) space