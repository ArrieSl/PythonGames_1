#by : arrie
import random
import os
import sys
#pip3 install playsound -> for music
from playsound import playsound


os.system('clear')
print("    **** Welcome to Rock Paper Scissors game ****    ")

#Function to exit the program
def exitt():
  os.system('clear')
  print(f' *** Result ***')
  print(f'{name} : {user_score}')
  print(f'CPU  : {cpu_score}')
  print(f'DRAW : {draw}')
  sys.exit(f" *** Thankyou for playing {name}! ***")

#initial value 
user_score = 0
cpu_score = 0
draw = 0 
tries = 0
max_tries = 5

#User name input
name = input('Enter your Name : ')

print (f" Welcome {name} ")

#Dictionary to select the Keys for CPU and User
choices={1:'rock',2:'paper',3:'scissor'}


while tries in range(max_tries):
  
  print(f'        Chances : {tries+1} out of {max_tries}')
  
  #CPU selects a random key from "choices" dictionary
  comp = random.choice(list(choices.keys()))

  #User input and pgm only accepts int value
  try:
    user = int(input('Enter your option 1 for rock , 2 for paper and 3 for scissor : '))
  except ValueError:
     print(f'*** ERROR : Only Integer Value allowed ***') 
     print(f"      {name} Select any from 1 and 3")
     continue
  
  #try block to check the input key is available in dictionary
  try :
    sel = choices[user]   
  except KeyError:
    print(f"  ****INVALID OPTION SELECTED, Entered value : {user} ****")
    print(f"      {name} Select any from 1 and 3")
    continue
  
  #Displays the values User and CPU selects
  print(f'        {name} selected {sel}')

  print(f'        CPU selected {choices[comp]}')

  #user_selection = rock
  if user == 1:
    if comp == 1:
      print('Draw')
      draw += 1
    elif comp == 2:
      print("You lose, try again")
      cpu_score += 1  
    else:
      print('You Won , Congratulations!!!')
      user_score += 1
      
  #user_selection = paper
  if user == 2:
    if comp == 1:
      print('You Won , Congratulations!!!')
      user_score += 1
      
    elif comp == 2:
      print('Draw')
      draw += 1
    else:
      print("You lose, try again")
      cpu_score += 1
  
  #user_selection = scissor
  if user == 3:
    if comp ==1:
      print("You lose, try again")
      cpu_score += 1
    elif comp == 2:
      print("You Won , Congratulations!!!")
      user_score += 1
      
    else:
      print("Draw")
      draw += 1
  
  tries = tries + 1
  #end of while loop

#Displays the result  
print(f'{name} You Won {user_score} times, You lose {cpu_score} times, Draw:{draw}')

#If condition to check the result and play music
if user_score > cpu_score :
  playsound("Firecrackers.wav")
elif user_score < cpu_score:
  playsound("lose.mp3")
elif user_score == cpu_score:
  playsound("draw.mp3")

#Calls the exitt function
exitt()
