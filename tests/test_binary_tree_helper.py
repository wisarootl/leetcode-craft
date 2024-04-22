from leetcode_craft.binary_tree_helper import build_binary_tree_from_array_representation


def test_build_binary_tree_from_array_representation():
    array_representation = [3, 9, 20, None, None, 15, 7]
    root = build_binary_tree_from_array_representation(array_representation)

    assert root.val == 3
    assert root.left.val == 9
    assert root.right.val == 20
    assert root.left.left is None
    assert root.left.right is None
    assert root.right.left.val == 15
    assert root.right.right.val == 7


def test_array_representation_empty_tail():
    # fmt: off
    array_representation = [
            1,  # depth = 0, n = 1
            None, 1,  # depth = 1, n = 2
            *[None] * 2, 1, 1,  # depth = 2, n = 4
            *[None] * 6, 1, 1,  # depth = 3, n = 8
            *[None] * 13, 1, *[None] * 2,  # depth = 4, n = 16
            *[None] * 27, 1, *[None] * 4,  # depth = 5, n = 32
        ]
    # fmt: on

    root = build_binary_tree_from_array_representation(array_representation)
    assert root.__repr__() == str(array_representation[:-4])


def test_binary_tree_node_repr():
    array_representation = [3, 9, 20, None, None, 15, 7]
    root = build_binary_tree_from_array_representation(array_representation)

    assert root.__repr__() == str(array_representation)


def test_binary_tree_equality():
    array_representation = [3, 9, 20, None, None, 15, 7]
    root = build_binary_tree_from_array_representation(array_representation)
    root_2 = build_binary_tree_from_array_representation(array_representation)

    assert root is not root_2
    assert root == root_2

    root_2.val = 5
    assert not root == root_2
    assert not root == 5


def test_empty_binary_tree():
    empty_root = build_binary_tree_from_array_representation([])
    assert empty_root is None
