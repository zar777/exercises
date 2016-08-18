def has_cycle(head):
    d = set()
    while head:
        if head.data in d:
            return 1
        else:
            d.add(head.data)
            head = head.next
    return 0
