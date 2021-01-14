
# search for element in array using iterator.

# search for element in array using binary search
# create fn: array_binary_search. takes two args, Array_to_search && element to find
# if not element return -1
# if element return indexof(element)
# 

def search_by_iterator(array: list, term: int) -> int :
  for element in array:
   if element == term:
     return array.index(element)
  
  if not term in array:
    return -1
  
  
def find_mid_list(array: list) -> int:
  return array[len(array) // 2]

def array_binary_search(array: list, term: int) -> int:
  mid = find_mid_list(array)
  if len(array) < 1 :
    return -1
  elif term == mid :
    return array.index(term)
  elif term > mid:
    array = array[mid:]
    array_binary_search(array, term)
  else: 
    array = array[:mid]
    array_binary_search(array, term)





  