# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        current_node = head
        nodes = []
        while current_node:
            if current_node in nodes:
                return True
            else:
                if current_node.next:
                    nodes.append(current_node)
                    current_node = current_node.next
                else:
                    return False