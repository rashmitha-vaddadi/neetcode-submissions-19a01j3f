# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cycle = set()
        listnode = head
        while listnode:
            if listnode in cycle:
                return True
            cycle.add(listnode)
            listnode = listnode.next
        return False
        