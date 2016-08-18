def CompareLists(headA, headB):
    while headA:
        if headA.data == headB.data:
            headA = headA.next
            headB = headB.next
        else:
            return 0
    if headA is None and headB is None:
        return 1
    else:
        return 0
