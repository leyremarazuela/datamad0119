def my_function(X):
  solutions = []
  for x in range(X, 5, -1):
    for y in range(X, 4, -1):
      for z in range(X, 3, -1):
        if (x*x==y*y+z*z):
          return(x)

X = input("What is the maximal length of the triangle side? Enter a number: ")

print("The longest side possible is " + str(my_function(int(X))))