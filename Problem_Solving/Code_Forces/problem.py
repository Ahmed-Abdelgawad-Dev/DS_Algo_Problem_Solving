class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:

    def merge_two_sorted_lists(self, list_one, list_two):
        head = current = Node(None)
        while list_one and list_two:
            if list_one.value < list_two.value:
                current.next, list_one = list_one, list_one.next
            else:
                current.next, list_two = list_two, list_two.next
            current = current.next
        current.next = list_one or list_two
        return head.next


sol = Solution()
sol.merge_two_sorted_lists([2, 4, 6], [1, 3, 5])
