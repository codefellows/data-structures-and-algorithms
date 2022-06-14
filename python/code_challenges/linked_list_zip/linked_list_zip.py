def zip_lists(a, b):
    current_a = a.head
    current_b = b.head
    temp_a = current_a.next
    temp_b = current_b.next
    while current_a.next and current_b.next:
        current_a.next = current_b
        current_b.next = temp_a
        current_a = temp_a
        current_b = temp_b
    if current_a.next and current_b.next:
        temp_a = current_a.next
        temp_b = current_b.next
    elif not current_a.next:
        current_a.next = current_b
    elif not current_b.next:
        current_a.next = current_b
        current_b.next = temp_a
    return a
