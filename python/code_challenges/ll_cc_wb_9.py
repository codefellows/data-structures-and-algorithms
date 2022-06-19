def linked_list_reverse(ll, new_ll = None)

	current = ll.head

	location = new_ll.head

	while current:

		location.value = current.value

		current = current.next

		location.next = location

	return new_ll
