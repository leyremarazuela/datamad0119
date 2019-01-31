"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""
def palabrasaleatorios(n,a,b):
  import random
  lista=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
  r = []
  while len(r)<n:
    palabra = ''
    if a < b:
      c = random.choice(range(a, b))
      for i in range(c):
        x = random.choice(lista)
        palabra += x
    elif a == b:
      c = a
      for i in range(c):
        x = random.choice(lista)
        palabra += x
    else:
      import sys
      sys.exit('Incorrect min and max string lengths. Try again.')
    r.append(palabra)
  return r


a = input('Enter minimum string length: ')
b = input('Enter maximum string length: ')
n = input('How many random strings to generate? ')

r = palabrasaleatorios(int(n), int(a), int(b))
print(r)