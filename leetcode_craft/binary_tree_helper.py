from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: Optional[float | int] = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.array_representation())

    def __eq__(self, other):
        if isinstance(other, TreeNode):
            return self.val == other.val and self.left == other.left and self.right == other.right
        return False

    def max_depth(self) -> int:
        def _max_depth(node: Optional["TreeNode"]) -> int:
            if node is None:
                return 0
            left_depth = _max_depth(node.left)
            right_depth = _max_depth(node.right)
            return max(left_depth, right_depth) + 1

        return _max_depth(self)

    def array_representation(self) -> list:
        max_depth = self.max_depth()
        nodes: list["TreeNode" | None] = [self]
        result = []

        for _ in range(1, max_depth + 1):
            level_nodes, level_values = [], []
            for node in nodes:
                if node:
                    level_values.append(node.val)
                    level_nodes.extend([node.left, node.right])
                else:
                    level_values.append(None)
                    level_nodes.extend([None, None])
            result.extend(level_values)
            nodes = level_nodes

        while result and result[-1] is None:
            result.pop()

        return result


def build_binary_tree_from_array_representation(nodes: list) -> TreeNode | None:
    if not nodes:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in nodes]

    for i in range(len(nodes)):
        node = nodes[i]
        if node is not None:
            left_child_idx = 2 * i + 1
            right_child_idx = 2 * i + 2

            node.left = nodes[left_child_idx] if left_child_idx < len(nodes) else None
            node.right = nodes[right_child_idx] if right_child_idx < len(nodes) else None

    return nodes[0]
