# soluzione non mia, consultata
def MergeLists(headA, headB):
    if headA is None and headB is None:
        return None
    if headA is None:
        return headB
    if headB is None:
        return headA
    if headA.data < headB.data:
        smaller_node = headA
        smaller_node.next = MergeLists(headA.next, headB)
    else:
        smaller_node = headB
        smaller_node.next = MergeLists(headA, headB.next)
    return smaller_node