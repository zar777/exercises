def Delete(head, position):
    if position == 0:
        head = head.next
        return head
    top = head
    count = 0
    while top:
        count += 1
        prev = head
        head = head.next
        if count == position:
            prev.next = head.next
            return top