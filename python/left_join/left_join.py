left = { 
  'fond': 'enamored',
  'wrath': 'anger',
  'diligent': 'employed',
  'guide': 'user'
}

right = {
  'fond': 'averse',
  'wrath': 'food',
  'guide': 'follow',
  'outfit': 'employed'
}

def join_left(hm1, hm2):
  matches = []
  values1 = list(hm1.values())
  values2 = list(hm2.values())
  keys1 = list(hm1.keys())
  keys2 = list(hm2.keys())

  for i in range(len(keys1)):
    for j in range(len(keys2)):
      print('i is: ', keys1[i])
      print('j is: ', keys2[j])
    #   if keys[1] in matches:
      if (keys1[i] == keys2[j]):
        to_append = [keys1[i], values1[i], values2[j]]
        matches.append(to_append)
        
    
    to_append = [keys1[i], values1[i], 'NULL']
    matches.append(to_append)

    # else:

    # for vals in range(len(matches)):
    #     print('vals in matches:', matches[vals][1])
    #     if (keys1[i] not in matches[vals][0]) and (values1[i] not in matches[vals][1]):
    #       # print(matches)
    #       to_append = [keys1[i], values1[i], 'NULL']
    #       matches.append(to_append)
    
  return matches

if __name__ == "__main__"
    print('This doesnt work yet!')
    print('returned', join_left(left, right))