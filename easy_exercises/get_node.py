def GetNode(head, position):
    count = 0
    top = head
    while head:
        head = head.next
        count += 1
    count -= position
    for i in xrange(count-1):
        top = top.next
    return top.data
