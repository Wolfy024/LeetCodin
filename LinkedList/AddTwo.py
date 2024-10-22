class ListNode:
    def __init__(self, val):
        self.val = None
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        tail = dummy
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            n1 = l1.val if l1 is not None else 0
            n2 = l2.val if l2 is not None else 0
            number = n1 + n2 + carry
            digit = number % 10
            carry = number // 10
            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        result = dummy.next
        return result
