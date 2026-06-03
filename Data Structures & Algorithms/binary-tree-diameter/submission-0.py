class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0  # height = 0 edges

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # Update diameter (number of edges)
            self.diameter = max(self.diameter, left_height + right_height)

            # Return height of subtree
            return 1 + max(left_height, right_height)

        dfs(root)
        return self.diameter
