

def insert_shift_array(n, array):
  """param1----> int param2---->array
     check length of array for even insert int at middle, if odd insert int at middle plus one
     
  """
  if not len(array) % 2:
    array.insert(round(len(array)/2), n)
    return array
  else:
    array.insert(int(len(array)/2 +1), n)
    return array

    