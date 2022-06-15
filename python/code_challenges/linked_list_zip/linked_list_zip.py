def zip_lists_starter(a, b):
    # To start lets make sure we have the data we are looking for. Its good to have catches for edge cases or things that could break the code.

    # If one of the linked lists is empty, lets just return the other.
    if a.head is None and b.head is None:
        return 'Need to provide at least 1 linked_list with values'

    elif a.head is None or b.head is None:
        return a or b
    # This will return whichever one of these is a truthy statement
    # If they are both empty, this will give None from one of them. That is why we wrote the previous statement.

    # Now we have two linked lists that will both have at least a head.

    current_1 = a.head
    current_2 = b.head

    # Head Nodes In Charge

    while current_1 or current_2:
        #At this point in the code we know this will run at least one time. We are setting this to the current and not just the head values because the heads only would create an infinite loop.
        #Here we do while current 1 AND current 2 which fixes the problem of having one list longer than the other one!

        temp_1 = current_1.next
        temp_2 = current_2.next
        #Note that we are assigning the temp values INSIDE the while loop here. Major key to preventing the infinite loop.

        current_1.next = current_2
        current_2.next = temp_1

        #Time to reassign the values here.

        current_1 = temp_1
        current_2 = temp_2

        #Remember how we were looking at the loops having two assignments? We go from linked a list thing one to linked list b thing 1 to linked list a thing 2. Now we slide down one in both lists and do the new v shift to the second list and back to the first. You had the right idea, but needed to assign the temp variables INSIDE the traversal loop where the magic happens.

    b.head = None
    #This will pretty much empty linked list b when we are done with the traversal.

    return a



def zip_lists(a, b):
    #This is the version that takes into account what happens if one list is longer than the other.

    if a.head is None and b.head is None:
        return 'Need to provide at least 1 linked_list with values'

    elif a.head is None or b.head is None:
        return a or b


    current_1 = a.head
    current_2 = b.head


    while current_1 and current_2:


        temp_1 = current_1.next
        temp_2 = current_2.next

        current_1.next = current_2

        if temp_1:
            current_2.next = temp_1
        #This is how we are checking if one list is longer than the other

        # We are assigning only temp 1 to a next value.
        # If temp 2 is none, the loop will break in the while current loop

        current_1 = temp_1
        current_2 = temp_2


    b.head = None


    return a



