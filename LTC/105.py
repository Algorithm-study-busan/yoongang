from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder:
            idx = inorder.index(preorder.pop(0))

            tree = TreeNode(inorder[idx])
            tree.left = self.buildTree(preorder[0 : idx], inorder[0 : idx])
            tree.right = self.buildTree(preorder[idx : ], inorder[idx + 1 : ])

            return tree

        