class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = [0]

        def height(node):
            if node is None:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            diameter[0] = max(
                diameter[0],
                left_height + right_height
            )

            return 1 + max(left_height, right_height)

        height(root)

        return diameter[0]