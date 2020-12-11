def insertShiftArray(list, num):
  if len(list) % 2 == 0:
    newList = []
    midpoint = len(list)//2
    newList = list[0:midpoint] + [num] + list[midpoint:]
    return newList
  else:
    newList = []
    midpoint = len(list)//2+1
    newList = list[0:midpoint] + [num] + list[midpoint:]
    return newList

# print(insertShiftArray)