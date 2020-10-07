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
      ch_list.append(char)
    file.close()
  # If user chooses to enter input via command line
  elif ch==2:
    print("Enter the characters : ")
    ch_list = list(map(str, input()))
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
