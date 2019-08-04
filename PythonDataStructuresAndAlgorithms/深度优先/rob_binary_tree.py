class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def rob(self, root):
        a = self.helper(root)
        return max(a[0], a[1])

    def helper(self, root):
        if root is None:
            return [0, 0]
        left = self.helper(root.left)
        right = self.helper(root.right)
        robValue = root.val + left[1] + right[1]
        skipValue = max(left[0], left[1]) + max(right[0], right[1])
        return [robValue, skipValue]
