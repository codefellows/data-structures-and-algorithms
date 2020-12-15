
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
  return array[round(len(array)/2)]

def array_binary_search(array: list, term: int) -> int:
  
  
  while len(array) >= 0:
    if term > find_mid_list(array):
      array = array[find_mid_list(array) : len(array)]
    elif term < find_mid_list(array):
      array = array[0 : find_mid_list(array)]
    elif term == find_mid_list(array):
      return array.index(term)
    else:
      return -1





  