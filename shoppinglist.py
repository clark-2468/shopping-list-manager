#import the two modules
import os
import time


#get a number from the user
def input_number():

  number=input("")
  #validation
  valid=False
  while not valid:
    if number.isnumeric():
      valid=True
    else:
      print("invalid")
      number=input("enter again ")
  return int(number)#change type


#subroutine to create a list
def create_a_file(index):

#bug here
  if int(check_no_of_lists()) == 0:
    index=1
  elif index == int(check_no_of_lists()+1):
    index = index+1
  else: index = index
  
  file_name = "Shopping list {}.txt" .format(index) #index indicate the number
  stream_when_creating=open(file_name,"w") #create
  stream_when_creating.write("{}\n" .format(file_name))#initialise
  stream_when_creating.close() 
  return file_name 


#write a string into the file
def open_for_write(file_name,item):

  stream_when_writing=open(file_name,"a")#a for append instead of w
  stream_when_writing.write("{}\n" .format(item)) #write a line of data and a blank line
  stream_when_writing.close()


#read a file
def open_for_read(file_name):

  stream_when_reading=open(file_name,"r")
  print("the text inside that is the following: ")
  
  data=" "
  while data:
    data=stream_when_reading.readline()#read line by line
    if data: 
      print(data)#print
      
  stream_when_reading.close()


#remove one item from a file
def remove_an_item(file_name,item_to_be_removed):
  #not finished yet
  print("done")

#delete a file
def remove(file_name):

  os.remove(file_name)
  print(file_name,"has been removed")


#print out a list of shoppinglists
def get_list_of_files():

  c_work_dir=os.getcwd() #get current working directory
  List=os.listdir(c_work_dir)
  print(List)
  return List


#check how many files are under the working directory
def check_no_of_lists():

  c_work_dir2=os.getcwd() #get current working directory
  nooffile=len(os.listdir(c_work_dir2))-1 #ignore mian.py
  return nooffile


#select a list
def Chooseshoppinglist(nooffile):
  
  print("There is {} lists in the system" .format(nooffile))
  get_list_of_files()
  print("Choose the list by enter the number")
  file_name="Shopping list {}.txt" .format(int(input_number()))
  print("{} has been selected " .format(file_name))
  return file_name


#user interface
def user_interface():
  
  users_option=0
  while users_option != 4:
    time.sleep(1)
    print("Welcome to your shopping list manager")
    time.sleep(1)
    print("What do you want to do?")
    print("1. Create a shopping list")
    print("2. Select a shopping list (add/remove an item or just check)")
    print("3. Delete a shopping list")
    print("4. Exit")
    #tell what they can do

    users_option=input_number()
    
    #1
    if users_option == 1:
      index = check_no_of_lists()+1
      file_name=create_a_file(index)
      print("{} has been created" .format(file_name))
      print("What do you want to do next? ")
    
    
    #2
    elif users_option == 2:
      #check how many files are there
      nooffile=check_no_of_lists()
      if nooffile != 0:

        file_name=Chooseshoppinglist(nooffile)#ask user to choose one that they want
      
        users_option2=0 #initialise opt2
        
        while users_option2 != 4:

          time.sleep(1)
          print("1. Add one item to your shopping list")
          print("2. Check your shopping list")
          print("3. Remove one item")
          print("4. Go Back")
          users_option2=int(input_number())

          if users_option2 == 1:
          
            print("type the item u want to add")
            item=input("")#get the item
            open_for_write(file_name,item)
            print("What do you want to do next? ")#ask next step
          
          elif users_option2 == 2:
            open_for_read(file_name)
            print("What do you want to do next? ")

          elif users_option2 == 3:
            #not finished yet
            open_for_read(file_name)
            item_to_be_removed=("{}\n" .format(input("what do you want to delete?")))
            remove_an_item(file_name,item_to_be_removed)
            print("What do you want to do next? ")

          elif users_option2 == 4:
            print("You are about to Exit")
            print("enter 4 again to confirm")#confirmation
            users_option2=input_number()
          
          else:
            print("invalid, enter again")
            users_option2=input_number()
      else: 
        print("no existing list, please create one first")

      print("What do you want to do next? ")


    #3
    elif users_option == 3:
      #check how many files are there
      
      nooffile=check_no_of_lists()
      if nooffile != 0:  #if there is file
        file_name = Chooseshoppinglist(nooffile)#choose
        remove(file_name)#delete
      else:
        print("no existing list, please create one first")
      print("What do you want to do next? ")


    #4
    elif users_option == 4:
      print("You are about to Exit")
      print("enter 4 again to confirm")
      users_option=input_number()
      

    else:
      
      print("invalid input, try again")
      users_option=input_number()
    
  print("Logged out!")





#run 
user_interface()