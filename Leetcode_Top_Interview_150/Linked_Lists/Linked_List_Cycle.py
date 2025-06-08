class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def linkedListCycle(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
        
    return False

nodeA = ListNode(1)
nodeB = ListNode(2)
nodeC = ListNode(3)
nodeD = ListNode(4)

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeA

print(linkedListCycle(nodeA))