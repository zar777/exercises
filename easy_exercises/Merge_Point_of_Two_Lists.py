def FindMergeNode(headA, headB):
    while headA.data == headB.data:
        if headA.data < headB.data:
            headA = headA.next
        elif headA.data > headB.data:
            headB = headB.next
    return headA.next.next.data



# trovato soluzione ma non l'ho capita
# def FindMergeNode(headA, headB):
#     curA = headA
#     curB = headB
#     while not curA == curB:
#         if curA.next is None:
#             curA = headB
#         else:
#             curA = curA.next
#         if curB.next is None:
#             curB = headA
#         else:
#             curB = curB.next
#     return curA.data