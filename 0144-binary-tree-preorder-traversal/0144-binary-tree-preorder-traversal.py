

class Solution:
    def preorderTraversal(self, root):
        result = []
        
        def preorder_helper(node):
            if not node:
                return
            result.append(node.val)
            preorder_helper(node.left)
            preorder_helper(node.right)

        preorder_helper(root)
        return result