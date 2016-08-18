def Insert(head, data):
    node = Node(data)
    node.next = head
    return node