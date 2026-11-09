# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #with the assumption that they are unique this would work but the values are not unquie.
        seen = set() 
        curr = head
        while curr:
            if curr.val in seen:
                return True
            seen.add(curr.val)
            curr = curr.next
        return False

        