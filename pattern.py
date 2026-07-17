"""
* 
* * 
* * * 
* * * * 
* * * * * 
"""

r = 5
for i in range(1, r+1):
  for j in range(1, i+1):
    print("*", end=" ");
  print();

"""
* * * * * 
* * * * 
* * * 
* * 
* 
"""
r = 5
for i in range (r, 0,-1):
  for j in range( i):
    print("*", end="  ");
  print();

"""
*****
*****
*****
*****
*****
"""
for i in range(5):
  for j in range(5):
    print("*", end="");
  print();

"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
"""
n = 6
for i in range(1,6):
  for j in range(1, i+1):
    print(j, end=" ");
  print();

"""
1 
2 2 
3 3 3 
4 4 4 4 
"""
n = 4
for i in range(1, n+1):
  for j in range(i):
    print(i, end=" ");
  print();

n=4
for i in range(1, n+1):
  for s in range(n,-i):
    print("-", end="");
  for j in range(i):
    print("*", end="");
  print();
n = 4
for i in range(1, n+1):
    print("  " * (n - i) + "*" * i);

n = 4
for i in range(1, n+1):
  print(" "*(2*(i-1))+ "*"*i);
