import math
#1
def hp():
  print("Hello, Python")
hp()
#2
def a(Enamul):
  print(Enamul)
a("Enamul Kabir")
#3
def add(a,b):
  return a+b
add(10,50)
#4
def default(a="Hello"):
  print(a)
default()
#5
def s(a):
  return a*a
print(s(4))
#6 problem
def list1(item):
  for i in item:
    print(i)
list1([10,11,12,30])
#7
def func7(a,b):
  return max(a,b)
print(func7(90,50))
#8
def even(a):
  if a%2==0:
    return True
  else:
    return False
print(even(5))
#9 problem
def a(*args):
  print(args[0])
  print(args[1])
  print(args)
a("Enamul","Kabir","Zishan")

#10
