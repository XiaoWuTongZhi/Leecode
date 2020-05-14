'''
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''
class ListNode:
    val : int

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return None
        start = ListNode(0)
        node = start
        carry = 0

        while (l1 or l2):
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = sum // 10
            rem = sum % 10
            node.next = ListNode(rem)
            node = node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry != 0:
            node.next = ListNode(1)
        return start.next

def print_node(node: ListNode):
    final = ''
    while node :
        final += '%d'%node.val
        node = node.next
    print(final)

if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    print_node(l1)
    print_node(l2)

    res_node = Solution.addTwoNumbers(l1=l1,l2=l2)
    print_node(res_node)
