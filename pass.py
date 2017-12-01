import string 
import random 

def passgen(length,number,symbols,caps):
  password = ''
  
  if number == True and symbols == True and caps == True:
    for i in range(length-3):
      x = random.randint(10,35)
      password += string.printable[x]
    y=random.randint(38,61)
    password= password+string.printable[y]
    password= password+string.printable[62]
    z=random.randint(0,9)
    password= password+string.printable[z]
  
  elif number == False and symbols == False and caps == False:
    for i in range(length):
      x = random.randint(10,35)
      password += string.printable[x]
  
  elif number == True and symbols == True and caps == False:
    for i in range(length-2):
      x = random.randint(10,35)
      password += string.printable[x]
    z=random.randint(0,9)
    password= password+string.printable[z]
    password= password+string.printable[62]
  
  elif number == True and symbols == False and caps == True:
    for i in range(length-2):
      x = random.randint(10,35)
      password += string.printable[x]
    z=random.randint(0,9)
    password= password+string.printable[z]
    y=random.randint(38,61)
    password= password+string.printable[y]
    
  elif number == True and symbols == False and caps == False:
    for i in range(length-1):
      x = random.randint(10,35)
      password += string.printable[x]
    z=random.randint(0,9)
    password= password+string.printable[z]
    
  elif number == False and symbols == False and caps == True:
    for i in range(length-1):
      x = random.randint(10,35)
      password += string.printable[x]
    y=random.randint(38,61)
    password= password+string.printable[y]
    
  elif number == False and symbols == True and caps == False:
    for i in range(length-1):
      x = random.randint(10,35)
      password += string.printable[x]
    password= password+string.printable[62]
    
  elif number == False and symbols == True and caps == True:
    for i in range(length-2):
      x = random.randint(10,35)
      password += string.printable[x]
    password= password+string.printable[62]
    y=random.randint(38,61)
    password= password+string.printable[y]
  
  return password
