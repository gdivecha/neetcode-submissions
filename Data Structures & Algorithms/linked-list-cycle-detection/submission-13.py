# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # - Let's try to figure out the desired solution here keeping in mind the
        #   following criteria:
        #   - You should aim for a solution with O(n) time and O(1) space, where n is
        #     the length of the given list.
        #   - We are dealing with linked lists
        # - There is a certain approach that is perfect for detecting cycles in a
        #   linked list -> The tortoise and hare algorithm
        #   - The premise is that if we have a pointer traverse through the linked
        #     list and another pointer traverse through the same list at twice
        #     the speed (traverse 2 nodes in a list at a time), then if there does
        #     end up being a cycle, then these 2 pointers will eventually
        #     converge and intersect at some point.
        
        # Algorithm:
        # - if head is None or head.next is None:
        #   - return false
        #   - Because an empty list can have 0 cycles and neither can a singleton list
        # - tortoise = head
        # - hare = head.next
        # - while hare.next is not None:
        #   - tortoise = tortoise.next
        #   - hare = hare.next.next
        #   - if tortoise is hare:
        #     - return true
        # - return false

        if head is None or head.next is None:
            return False
        tortoise = head
        hare = head.next
        while hare is not None:
            tortoise = tortoise.next
            if hare.next is None:
                return False
            else:
                hare = hare.next.next
            if tortoise is hare:
                return True
        return False