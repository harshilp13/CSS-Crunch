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