# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # - Let's look at the required critera first:
        #   - You should aim for a solution with O(n) time and O(n) space, 
        #     where n is the number of nodes in the tree.
        #   - Tree problem
        # - Let's look at the desired behavior and maybe come up with the algo
        #   along with it:
        #   - I think we should use recursion because we need sort of a depth first
        #     search to find the longest path, get to the bottom of the longest path,
        #     and propogate the max depth forward
        #   - e.g. Input: root = [1,2,3,null,null,4]
        #     - First of all, we need to figure out the positioning and indexing
        #       format of the array we are given
        #     - [1,2,3,null,null,4] means we look att he diagram from the first example
        #       - left of index 0 is at index 1
        #       - right of index 0 is at index 2
        #       - left of index 1 is at index 3
        #       - right of index 1 is at index 4
        #       - left of index 2 is at index 5
        #       - right of index 2 is at index 6 which does not exist in the array
        #         but should as a Null value which we will need to account for
        #         - I think that the left and right (Null children) of 2 also wouldn't
        #           have been mentioned in the array if 4 did not exist as a child
        #           of 3 which is an element later in the array
        #         - This means that a Null value is only not mentioned in the array
        #           if it is the end leaf of a branch so we don't have to worry about
        #           a Null not being mentioned in between 2 non-null values in the array
        #     - So, we can come up with the formula that in the tree array:
        #       - left(index) = (2 * index) + 1
        #       - right(index) = 2 * (index + 1)
        #     - Let's come up with the behavior now - since we are using recursion,
        #       I usually like to go backwards from the point where the recursion
        #       triggers a return value:
        #       - @ index = 5 -> root[5] = 4:
        #         - Since 4 does not have any children and both are Null, we return a 1
        #         - We simply check whether 4's left and right children indices exist
        #           or that of they do exist, they're null
        #       - @ index = 2 -> root[2] = 3:
        #         - Before the recursive call (4 hasn't been called yet):
        #           - If left child exists (index is within the array or the child at
        #             the left child index is a non-Null):
        #             - leftDepth = maxDepth(..)
        #         - After the recursive call (After 4 was called):
        #
        #     ==============I just realized that the input was given in the form
        #                   of array just for ease of asking the question. It is
        #                   actually already in fact given in the form of a linked
        #                   list. Nothing changes except for the array approach.========
        #      
        #     - Let's come up with the behavior now - since we are using recursion,
        #       I usually like to go backwards from the point where the recursion
        #       triggers a return value:
        #       - @ node4:
        #         - leftChildExists = node4.left is not Null = false in this case
        #         - rightChildExists = node4.right is not Null = false in this case
        #         - Since leftChildExists and rightChildExists are both false:
        #           - return 1
        #       - @ node3:
        #         - Before the recursive call (4 hasn't been called yet):
        #           - leftChildExists = node3.left is not Null = true in this case
        #           - rightChildExists = node3.right is not Null = false in this case
        #           - if leftChildExists which is true:
        #             - leftMaxDepth = maxDepth(node3.left) which should have returned 1
        #           - if rightChildExists which is false:
        #             - rightMaxDepth = 0
        #         - After the recursive call (After 4 was called):
        #           - We find the max depth so far between leftMaxDepth & rightMaxDepth:
        #             plus (+) 1 which becomes 2
        #       - @ node2:
        #         - leftChildExists = node2.left is not Null = false in this case
        #         - rightChildExists = node2.right is not Null = false in this case
        #         - Since leftChildExists and rightChildExists are both false:
        #           - return 1
        #       - @ node1:
        #         - Before the recursive call (2 and 3 haven't been called yet):
        #           - leftChildExists = node1.left is not Null = true in this case
        #           - rightChildExists = node3.right is not Null = true in this case
        #           - if leftChildExists which is true:
        #             - leftMaxDepth = maxDepth(node1.left) which should have returned 2
        #           - if rightChildExists which is false:
        #             - rightMaxDepth = maxDepth(node1.right) which should've returned 1
        #         - After the recursive call (After 2 and 3 were called):
        #           - We find the max depth so far between leftMaxDepth & rightMaxDepth:
        #             plus (+) 1 which becomes 3

        # Algorithm:
        # - leftChildExists = root.left is not Null
        # - rightChildExists = root.right is not Null
        # - if not leftChildExists and not leftChildExists:
        #   - rerturn 1
        # - leftMaxDepth = 0
        # - rightMaxDepth = 0
        # - if leftChildExists:
        #   - leftMaxDepth = maxDepth(root.left)
        # - if rightChildExists:
        #   - rightMaxDepth = maxDepth(root.right)
        # - return max((leftMaxDepth + 1),(rightMaxDepth + 1))

        # if root is None:
        #     return 0
        # leftChildExists = root.left is not None
        # rightChildExists = root.right is not None
        # if not leftChildExists and not leftChildExists:
        #     return 1
        # leftMaxDepth = 0
        # rightMaxDepth = 0
        # if leftChildExists:
        #     leftMaxDepth = self.maxDepth(root.left)
        # if rightChildExists:
        #     rightMaxDepth = self.maxDepth(root.right)
        # return max((leftMaxDepth + 1),(rightMaxDepth + 1))

        # - Only 3/29 test cases passed:
        # - How about instead of return a 1 whenever a both children do not exist,
        #   we return a 0 by actually going into the Null child
        
        # Algorithm:
        # - if root is Null:
        #   - return 0
        # - leftMaxDepth = 0
        # - rightMaxDepth = 0
        # - if root.left:
        #   - leftMaxDepth = maxDepth(root.left)
        # - if root.right:
        #   - rightMaxDepth = maxDepth(root.right)
        # - finalMaxDepth = max(leftMaxDepth, rightMaxDepth) 
        # - return (finalMaxDepth + 1)

        if root is None:
            return 0
        leftMaxDepth = 0
        rightMaxDepth = 0
        if root.left:
            leftMaxDepth = self.maxDepth(root.left)
        if root.right:
            rightMaxDepth = self.maxDepth(root.right)
        finalMaxDepth = max(leftMaxDepth, rightMaxDepth) 
        return (finalMaxDepth + 1)

