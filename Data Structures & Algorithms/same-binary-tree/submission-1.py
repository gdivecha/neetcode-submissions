# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def preOrderTraversal(self, traversal: List[Optional[int]], node: Optional[TreeNode]) -> None:
        if node is None:
            traversal.append(None)
        else:
            traversal.append(node.val)
            self.preOrderTraversal(traversal, node.left)
            self.preOrderTraversal(traversal, node.right)

    def postOrderTraversal(self, traversal: list[int], node: Optional[TreeNode]) -> None:
        if node is None:
            traversal.append(None)
        else:
            self.preOrderTraversal(traversal, node.left)
            self.preOrderTraversal(traversal, node.right)
            traversal.append(node.val)

    def inOrderTraversal(self, traversal: list[int], node: Optional[TreeNode]) -> None:
        if node is None:
            traversal.append(None)
        else:
            self.preOrderTraversal(traversal, node.left)
            traversal.append(node.val)
            self.preOrderTraversal(traversal, node.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # - Let's look at the criteria we need:
        #   - You should aim for a solution with O(n) time and O(n) space, 
        #     where n is the number of nodes in the tree.
        #   - Tree Problem
        # - As far as I remember from COE 428, there are 3 ways to traverse
        #   through a tree and I think if we use traversal methods, we can use
        #   that to compare the results of the traversal between the 2 trees
        # - What are the 3 traversal methods under depth first search:
        #   - Pre-order
        #   - In-order
        #   - Post-order
        # - Let's see how the traversal prints the trees:
        #   e.g. [1,2,3,4,5,6] or:     1
        #                           /     \
        #                         2         3
        #                       / |         | \
        #                     4   5         6   N
        #                   / |   | \       | \
        #                  N  N   N  N      N  N   
        #
        #   - Pre-order: 1,2,4,5,3,6
        #   - Post-order: 4,5,2,6,3,1
        #   - In-order: 4,2,5,1,6,3
        # - So how would this be helpful?
        #   - We can make another method under Solution called one of these
        #     traversal methods and call that same method for each
        #     of the 2 trees and compare the results, then we get the answer
        
        pWalk = []
        qWalk = []

        self.preOrderTraversal(pWalk,p)
        self.preOrderTraversal(qWalk,q)

        # self.inOrderTraversal(pWalk,p)
        # self.inOrderTraversal(qWalk,q)

        # self.postOrderTraversal(pWalk,p)
        # self.postOrderTraversal(qWalk,q)

        return pWalk==qWalk





