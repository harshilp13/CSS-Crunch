# CSS - Crunch wordlister miniature version implementation 
# Contributors : KJSCE LY Comps B 
                #  1711105 Jaisingh Rajbhar
                #  1711126 Ravishankar Yadav
                #  1711127 Harshil Patel
                #  1711128 Deep Shah

from itertools import permutations
import operator as op
from functools import reduce
from os.path import exists
import os

# Computing number of possible passwords that will be generated
def number_passwords(length,min,max):   
  sum=0
  for _ in range(min,max+1):
    sum += PermutationCoeff(length, _)
  print("The number of possible permutations that will be generated :  ",sum,"\n")
  print("----------------------------------------------------------")
  return


# Function to compute value of npr 
def PermutationCoeff(n, r): 
	coeff = 1
	# Compute n! and (n-k)! 
	for i in range(0,r): 
		coeff *= n-i
	return coeff 
 

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


if __name__ == '__main__':
  ch = int(input("Enter input via 1.File 2.Runtime : "))
  # If user wishes to enter input via input file
  if ch==1:
    min=int(input("Enter minimum length : "))
    max=int(input("Enter maximum length : "))
    file = open("input.txt", "r")
    ch_list=[]
    while 1: 	
      char = file.read(1)		 
      if not char: 
        break
      ch_list.append(char)	
      print(char,'\n') 
    file.close()
  # If user chooses to enter input via command line
  elif ch==2:
    print("Enter the characters : ")
    ch_list = list(map(str, input()))
    print("You entered : ",ch_list)
    min=int(input("Enter minimum length : "))
    max=int(input("Enter maximum length : "))
  # Invalid choice
  else:
    print("Enter valid input")
  
  # printing the number of passwords that will be generated
  number_passwords(len(ch_list),min,max)

  f=open("output.txt", "w")
  f.write('\n')
  for _ in range(min,max+1):
    if ( _ <= len(ch_list)):
      output=list(permutations(ch_list,_))
      for x in output:
        x=list(x)
        # print(''.join(x))
        string= ''.join(x)
        with open("output.txt", 'a') as file: 
          file.write(string+"\t")
     
  print("\nOUTPUT written to output.txt !!!")
  print("Output File size : ",os.stat('output.txt').st_size,"Bytes")

