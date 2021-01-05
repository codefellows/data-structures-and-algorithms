from linked_list.linked_list import Node, LinkedList
version = 1

def zip_lists(ll_one, ll_two):
  leader = ll_one.head
  follow = ll_two.head
  temp_next_of_two = ''

  while ll_one and ll_two: # may actually need to be `and`
    if not leader.next and follow.next:
      return f'cannot zip two empty lists, please add nodes to either list and try again'

    else:
      if not leader.next:
        leader.next = follow.value
        return ll_one.head
      elif not follow.next:
        ll_one.insert_after(leader, follow.value)
        return ll_one.head
      else:
        temp_next_of_two = follow.next 
        ll_one.insert_after(leader.value, follow.value)
        leader = leader.next.next 
        follow  = temp_next_of_two
  
  return ll_one.head

