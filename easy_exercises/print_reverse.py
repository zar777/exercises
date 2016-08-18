def ReversePrint(head):
    elements = []
    while head:
        elements.append(head.data)
        head = head.next
    for i in xrange(len(elements)):
        print elements.pop()