print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')
a = str(input('Please choose your first number (zero to five): '))
b = str(input('What do you want to do? plus or minus: '))
c = str(input('Please choose your second number (zero to five): '))

lista = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten","negative five", "negative four", "negative three", "negative two", "negative one"]
operacion = ["plus", "minus"]

if a in lista and c in lista and b in operacion:
  if b == "plus":
    x = lista.index(a)
    y = lista.index(c)
    z = x + y
    resultado = lista[z]
    print(a + " " + b + " " + c + " " + "equals" + " " + resultado)
  elif b == "minus":
    x = lista.index(a)
    y = lista.index(c)
    z = x - y
    resultado = lista[z]
    print(a + " " + b + " " + c + " " + "equals" + " " + resultado)
else:
  print("I am not able to answer this question. Check your input.")

print("Thanks for using this calculator, goodbye :)")