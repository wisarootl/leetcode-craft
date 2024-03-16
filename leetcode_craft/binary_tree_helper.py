from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        if not self:
            return str([])

        result = []
        queue = deque([self])

        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        # Remove trailing nulls from the array representation
        while result and result[-1] is None:
            result.pop()

        return str(result)

    def __eq__(self, other):
        if isinstance(other, TreeNode):
            return self.val == other.val and self.left == other.left and self.right == other.right
        return False


def build_binary_tree_from_array_representation(nodes: list):
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1

    while queue and i < len(nodes):

        current_node = queue.popleft()

        if nodes[i] is not None:
            current_node.left = TreeNode(nodes[i])
            queue.append(current_node.left)
        i += 1

        if i < len(nodes) and nodes[i] is not None:
            current_node.right = TreeNode(nodes[i])
            queue.append(current_node.right)
        i += 1

    return root
