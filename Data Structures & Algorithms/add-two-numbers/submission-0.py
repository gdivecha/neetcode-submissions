# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # - You should aim for a solution with O(m + n) time and O(1) space, 
        #   where m is the length of list l1 and n is the length of list l2.
        # - Linked List problem
        
        # Algorithm:
        # - Since both lists are non-empty, we know we don't need to worry about
        #   the edge case of either being empty and returning a chopped value
        # - l1Pointer = l1
        # - l2Pointer = l2
        # - finalAnswerHead = NULL
        # - finalPointer = NULL
        # - carryOver = 0
        # - while l1Pointer or l2Pointer:
        #   - sum = carryOver
        #   - if l1Pointer:
        #     - sum += l1Pointer.val
        #     - l1Pointer = l1Pointer.next
        #   - if l2Pointer:
        #     - sum += l2Pointer.val
        #     - l2Pointer = l2Pointer.next
        #   - carryOver = sum // 10
        #   - remainder = sum % 10
        #   - finalNumNode = ListNode(remainder,NULL)
        #   - if finalAnswerHead is NULL:
        #     - finalAnswerHead = finalNumNode
        #     - finalPointer = finalAnswerHead
        #   - else:
        #     - finalPointer.next = finalNumNode
        #     - finalPointer = finalPointer.next
        # - if carryOver > 0:
        #   - finalNumNode = ListNode(carryOver,NULL)
        #   - finalPointer.next = finalNumNode


        l1Pointer = l1
        l2Pointer = l2
        finalAnswerHead = None
        finalPointer = None
        carryOver = 0
        while l1Pointer or l2Pointer:
            currentSum = carryOver
            if l1Pointer:
                currentSum += l1Pointer.val
                l1Pointer = l1Pointer.next
            if l2Pointer:
                currentSum += l2Pointer.val
                l2Pointer = l2Pointer.next
            carryOver = currentSum // 10
            remainder = currentSum % 10
            finalNumNode = ListNode(remainder,None)
            if finalAnswerHead is None:
                finalAnswerHead = finalNumNode
                finalPointer = finalAnswerHead
            else:
                finalPointer.next = finalNumNode
                finalPointer = finalPointer.next
        if carryOver > 0:
            finalNumNode = ListNode(carryOver,None)
            finalPointer.next = finalNumNode
        return finalAnswerHead






