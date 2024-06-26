from typing import Any, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: Any = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
            if current:
                result.append(" -> ")
        return "".join(result)

    def __eq__(self, other):
        current_self = self
        current_other = other

        while current_self and current_other:
            if current_self.val != current_other.val:
                return False
            current_self = current_self.next
            current_other = current_other.next

        return current_self is None and current_other is None


def build_linked_list(nodes: list) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy

    for val in nodes:
        current.next = ListNode(val)
        current = current.next

    return dummy.next
