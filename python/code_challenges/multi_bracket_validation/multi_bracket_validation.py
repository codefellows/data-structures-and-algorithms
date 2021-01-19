

def multi_bracket_validation(input_str):
  if input_str == '':
    return f'Cannot validate empty string'

  if type(input_str) is not str:
    return f'Cannot validate input of type: {type(input_str)}'
  
  opens = 0
  closes = 0
  
  for char in input_str:
    
    if char == '('  or char == '{' or char == '[':
      opens += 1
      
    elif char == ')' or char == '}' or char == ']':
      closes += 1
      
    else:
      continue
  
  if opens == closes:
    return True
  else: 
    return False
  