# Function to compute value of npr 
import math 
def fact(n):  
    if (n <= 1): 
        return 1
          
    return n * fact(n - 1)  
  
def PermutationCoeff(n, r):  
      
    return math.floor(fact(n) /
                fact(n - r))

 

def read_through_file():
  ch_list = []
  filename = input("ENter the filename = ")
  # if (!(exists(filename))):
  # #   print("Invalid filename\nExitting program")
  # #   exit()
  f= open(filename,"r")
  f.read()
  for _ in f:
    ch_list.append(_)
  f.close()
  return ch_list
