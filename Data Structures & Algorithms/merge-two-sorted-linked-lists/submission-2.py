# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # - Let's go through the criteria for this question:
        #   - You should aim for a solution with O(n + m) 
        #     time and O(1) space, where n is the length of 
        #     list1 and m is the length of list2.
        #   - We are dealing with linked lists
        # - Let's try to figure out the desired behavior from surface level
        #   - e.g. list1 = 1 -> 2 -> 4, list2 = 1 -> 3 -> 5
        #     - l1Iterator points to list1 -> list1 -> (1 -> 2 -> 4)
        #     - l2Iterator points to list2 -> list2 -> (1 -> 3 -> 5)
        #     - mergedList = []
        #     - @ l1Iterator.val = 1 & l2Iterator.val = 1:
        #       - Is l1Iterator.val < l2Iterator.val? No:
        #         - mergedList adds l2Iterator = [1] by making 
        #           mergedListIterator point to l2Iterator
        #         - We iterate to the next node in list2 so l2Iterator.next = 3
        #     - @ l1Iterator.val = 1 & l2Iterator.val = 3:
        #       - l1Iterator.val < l2Iterator.val? Yes:
        #         - mergedList adds l1Iterator = [1,1] by making 
        #           mergedListIterator point to l1Iterator
        #         - We iterate to the next node in list1 so l1Iterator.next = 2
        #     - @ l1Iterator.val = 2 & l2Iterator.val = 3:
        #       - l1Iterator.val < l2Iterator.val? Yes:
        #         - mergedList adds l1Iterator = [1,1,2] by making 
        #           mergedListIterator point to l1Iterator
        #         - We iterate to the next node in list1 so l1Iterator.next = 4
        #     - @ l1Iterator.val = 4 & l2Iterator.val = 3:
        #       - l1Iterator.val < l2Iterator.val? Yes:
        #         - mergedList adds l1Iterator = [1,1,2,3,4] by making 
        #           mergedListIterator point to l1Iterator
        #         - We iterate to the next node in list1 so l1Iterator.next = Null
        #     - @ l1Iterator Null & l2Iterator.val = 5:
        #       - l1Iterator.val < l2Iterator.val? No:
        #         - mergedList adds l1Iterator = [1,1,2,3,4,5] by making 
        #           mergedListIterator point to l2Iterator
        #         - We iterate to the next node in list2 so l2Iterator.next = Null
        #     - @ l1Iterator Null & l2Iterator = Null:
        #       - We exit the loop
        #     - We return the mergedList head
        
        # - Algorithm:
        #   - l1Iterator = list1
        #   - l2Iterator = list2
        #   - mergedList = Null
        #   - mergedListIterator = mergedList
        #   - While at least one of l1Iterator or l2Iterator is not Null:
        #     - l1IteratorIsNonNull = l1Iterator is not None
        #     - l2IteratorIsNonNull = l2Iterator is not None
        #     - If l1IteratorIsNonNull and l1IteratorIsNonNull
        #       - If l1Iterator.val < l2Iterator.val:
        #         - If mergedList is Null:
        #           - mergedList = l1Iterator
        #         - Else:
        #           - mergedListIterator.next = l1Iterator
        #         - l1Iterator = l1Iterator.next
        #         - mergedListIterator = mergedListIterator.next
        #       - Else:
        #         - If mergedList is Null:
        #           - mergedList = l2Iterator
        #         - Else:
        #           - mergedListIterator.next = l2Iterator
        #         - l2Iterator = l2Iterator.next
        #         - mergedListIterator = mergedListIterator.next
        #     - Else if l1IteratorIsNonNull:
        #       - If mergedList is Null:
        #         - mergedList = l1Iterator
        #       - Else:
        #         - mergedListIterator.next = l1Iterator
        #       - l1Iterator = l1Iterator.next
        #       - mergedListIterator = mergedListIterator.next
        #     - Else if l2IteratorIsNonNull:
        #       - If mergedList is Null:
        #         - mergedList = l2Iterator
        #       - Else:
        #         - mergedListIterator.next = l2Iterator
        #       - l2Iterator = l2Iterator.next
        #       - mergedListIterator = mergedListIterator.next
        #   - Return mergedList

        l1Iterator = list1
        l2Iterator = list2
        mergedList = None
        mergedListIterator = None
        while l1Iterator or l2Iterator:
            l1IteratorIsNonNull = l1Iterator is not None
            l2IteratorIsNonNull = l2Iterator is not None
            nodeToAttach = None
            if l1IteratorIsNonNull and l2IteratorIsNonNull:
                nodeToAttach = l1Iterator if l1Iterator.val < l2Iterator.val else l2Iterator
            elif l1IteratorIsNonNull:
                nodeToAttach = l1Iterator
            elif l2IteratorIsNonNull:
                nodeToAttach = l2Iterator
            if mergedList is None:
                mergedList = nodeToAttach
                mergedListIterator = mergedList
            else:
                mergedListIterator.next = nodeToAttach
                mergedListIterator = mergedListIterator.next
            if nodeToAttach is l1Iterator:
                l1Iterator = l1Iterator.next
            else:
                l2Iterator = l2Iterator.next
        return mergedList
            
