# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        res_str = str(list_node_to_num(l1) + list_node_to_num(l2))[::-1]
        res = ListNode(res_str[0])

        p = res
        for i in res_str[1:]:
            n = ListNode(int(i))
            p.next = n
            p = n

        return res


def list_node_to_num(list_node):
    if list_node is None:
        return 0

    s = ""
    while list_node is not None:
        s += str(list_node.val)
        list_node = list_node.next
    return int(s[::-1])
