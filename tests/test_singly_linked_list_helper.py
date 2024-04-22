from leetcode_craft.singly_linked_list_helper import ListNode, build_linked_list


def test_build_linked_list():
    arr = [1, 2, 3, 4, 5]
    head = build_linked_list(arr)

    assert head.val == 1
    assert head.next.val == 2
    assert head.next.next.val == 3
    assert head.next.next.next.val == 4
    assert head.next.next.next.next.val == 5
    pass


def test_linked_list_repr():
    arr = [1, 2, 3, 4, 5]
    head = build_linked_list(arr)
    assert head.__repr__() == "1 -> 2 -> 3 -> 4 -> 5"


def test_linked_list_eq():
    arr = [1, 2, 3, 4, 5]
    head = build_linked_list(arr)
    head_2 = build_linked_list(arr)
    assert head is not head_2
    assert head == head_2


def test_linked_list_not_eq():
    arr = [1, 2, 3, 4, 5]
    head = build_linked_list(arr)

    arr_2 = [1, 2, 3, 4, 6]
    head_2 = build_linked_list(arr_2)
    assert head is not head_2
    assert head != head_2
