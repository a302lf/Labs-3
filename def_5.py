def unit (numb):
  match(numb):
    case 0: part =''
    case 1: part ='one'
    case 2: part ='two'
    case 3: part ='three'
    case 4: part ='four'
    case 5: part ='five'
    case 6: part ='six'
    case 7: part ='seven'
    case 8: part ='eight'
    case 9: part ='nine'
  return part

def dozen (numb):
  match(numb):
    case 0: part =''
    case 2: part ='twenty'
    case 3: part ='thirty'
    case 4: part ='fourty'
    case 5: part ='fifty'
    case 6: part ='sixty'
    case 7: part ='seventy'
    case 8: part ='eighty'
    case 9: part ='ninety'
  return part

def especial(numb):
  match(numb):
    case 0: part ='ten'
    case 1: part ='eleven'
    case 2: part ='twenteen'
    case 3: part ='thirteen'
    case 4: part ='fourteen'
    case 5: part ='fifteen'
    case 6: part ='sixteen'
    case 7: part ='seventeen'
    case 8: part ='eighteen'
    case 9: part ='nineteen'
  return part

def value(numb):
  match(numb):
    case 0: part ='hundred'
    case 1: part ='thousand'
    case 2: part ='million'
    case 3: part ='billion'
    case 4: part ='trillion'
  return part

def valency(fullnumb): 
  countnumb = 0
  while fullnumb > 0:
    fullnumb=fullnumb//10
    countnumb +=1
  return countnumb

def decription(trio):
  decr = []
  first = trio//100
  second = (trio%100)//10
  third = trio%10
  decr.append(unit(first))
  if second > 1:
    decr.append(dozen(second))
    decr.append(unit(third))
  else: 
    match(second):
      case 1:
        decr.append(especial(third))
      case 0:
        decr.append(unit(third))
  return decr

def add_value(trio, step, decr):
  if (trio>99):
    decr.insert(1, value(0))
  if (step>3) and (trio!=0):
    decr.append(value(step//3-1))
  return decr

def full_decription(fullnumb):
  fulldecr = []
  strfulldecr = ''
  if fullnumb==0: fulldecr.append('zero')
  countnumb = valency(fullnumb) 
  while (countnumb%3)!=0:
    countnumb+=1
  for step in range(3, countnumb+1, 3):
    decr = []
    strdecr = ''
    trio = (fullnumb%(10**step))//(10**(step-3))
    decr = decription(trio) 
    decr = add_value(trio, step, decr)
    strdecr = ' '.join(decr)
    fulldecr.insert(0,strdecr)
  strfulldecr=' '.join(fulldecr)
  return strfulldecr

