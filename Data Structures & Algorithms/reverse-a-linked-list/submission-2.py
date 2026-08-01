# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # - Let's visualize the process we desire
        #   - First we need to keep in mind the following criteria:
        #     - You should aim for a solution with O(n) time and O(1) space, 
        #       where n is the length of the given list.
        #     - Let's use the recursive approach
        #   - e.g. N1 -> N2 -> N3 -> N4 -> NULL
        #     - We want the recursion breaker to get triggered when the NULL is
        #       detected and we want N4 to point towards N3
        #     - Let's look at that trigger so we will start backwards from the
        #       trigger back to the recursive call:
        #       - We want @ N3:
        #         - is N3.next.next which is pretty much (N4.next) == NULL? Yes:
        #           - We need N3 to be the one that we use to detect not N3 directly
        #             because of the following
        #           - Hold a variable called head = N3.next or N4
        #           - N3.next.next = N3 meaning N4.next = N3
        #           - We also want N3.next = NULL
        #           - This is what the list looks like now:
        #             N1 -> N2 -> N3 <- N4
        #                            -> NULL 
        #             meaning N3 points to NULL but both N2 and N4 point to N3
        #           - We return the head by doing "return head"
        #       - Working backwards with pointer @ N2:
        #         - Before the recursive call @ N2 for N3:
        #           - is N2.next.next which is pretty much (N3.next) == NULL? No:
        #             - We do head = recursively call the revereseList(N2.next)
        #         - After we recursively call the same function but for the next node 
        #           - N2.next.next = N2 meaning N3.next = N2
        #           - We also want N2.next = NULL
        #           - This is what the list looks like now:
        #             N1 -> N2 <- N3 <- N4
        #                      -> NULL 
        #             meaning N2 points to NULL but both N1 and N3 point to N2
        #           - We return the head by doing "return head"
        #       - Working backwards with pointer @ N1:
        #         - Before the recursive call @ N1 for N2:
        #           - is N1.next.next which is pretty much (N2.next) == NULL? No:
        #             - We do head = recursively call the revereseList(N1.next)
        #         - After we recursively call the same function but for the next node 
        #           - N1.next.next = N1 meaning N2.next = N1
        #           - We also want N1.next = NULL
        #           - This is what the list looks like now:
        #             N1 <- N2 <- N3 <- N4
        #                -> NULL 
        #             meaning N1 points to NULL but N2 points to N2
        #           - Keep in mind that this is essentially:
        #             N4 -> N3 -> N2 -> N1 -> NULL
        #           - We return the head by doing "return head"

        # Algorithm:
        # - if head is None or head.next is None: (for singleton list of empty list)
        #   - return head (returns singleton head for singleton list and NULL for 
        #     empty list)
        # - newHead = NULL
        # - if head.next.next is NULL:
        #   - newHead = head.next
        # - else:
        #   - newHead = reverseList(head.next)
        # - head.next.next = head
        # - head.next = NULL
        # - return newHead

        if head is None or head.next is None:
            return head
        newHead = None
        if head.next.next is None:
            newHead = head.next
        else:
            newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead
