# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_iter = iter(preorder)
        in_iter = iter(inorder)
        
        def build(stop=None):
            if not hasattr(build, 'curr_in'):
                build.curr_in = next(in_iter, None)
            if build.curr_in == stop:
                return None
            
            val = next(pre_iter)
            node = TreeNode(val)
            node.left = build(val)
            build.curr_in = next(in_iter, None)
            node.right = build(stop)
            return node
            
        return build()