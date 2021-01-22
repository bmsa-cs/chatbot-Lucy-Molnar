"""
Chatbot
Author: Lucy Molnar 
Period/Core: 2

"""

import os
import importlib.util

import random

def run_tests():
  """
  This function will check for the pytest module
  before calling it to run the included tests.py
  """
  if importlib.util.find_spec('pytest') is None: # Check if pytest is installed
    os.system('python3 -m pip install -q pytest')

  command = "python3 -m pytest --tb=line -v -s tests.py"
  print(command)
  os.system(command)

def main():
  """This function contains all code for the chatbot."""
  print("Hello there i'm Lucy Molnar and I am a student at a local college and I need to interview some people for a project I was hoping I could ask you some questions.")

print(" ")

print("Ok why don't I start by asking you some questions.")

print(" ")

Qestion1 = input("Ok question one whats your name?")
print("What an awesome name nice to meet you!")

Question2 = input("Next whats your zodiac sign?")
print("Thats so cool!")

Question3 = input("Third question are you afraid of snakes?")
if (Question3 == "yes" or Question3 == "yep"):
  print("It's ok i'm afraid of them too! They are sooo scary!")
elif (Question3 == "no" or Question3 == "nope"):
  print("Yeah i'm not afraid of them either there not that scary.")
else:
  print("I used to be afraid of them but not anymore.")

Question4 = input("Ok one more question after this Are you a dog or a cat person?")
if (Question4 == "dog" or Question4 == "puppy"):
  print("Thats so cool me too I love dogs so much I actually have two of my own!")
elif(Question4 == "cat" or Question4 == "kitty"):
  print("Wow me too! I have always been a cat person I happen to own three")
else:
  print("Oh cool I think both are great.")

  Question5 = input("Ok now for the last question. What color are your eyes?")
  if (Question5 == "brown" or Question5 == "Blue"):
    print("Thats so cool! I wish my eyes were that color!")
  elif(Question5 == "Green" or Question5 == "Hazel"):
    print("Wow no fair I wish my eyes could be that color!")
  else:
    print("Omg what a unique color! I wish my eyes were that color!")

  Question6 = input("Ok now for the last question. How old are you?")
  if (Question6 == "15" or Question6 == "14"):
    print("cool.")
  elif(Question6 == "13" or Question6 == "16"):
    print("awesome.")
  else:
    print("Nice.")

Question7 = input("Oops wait sorry I have just one more small question to ask if you wouldn't mind... Did you enjoy this interview? I worked really hard on coming up with these questions.")
if (Question7 == "yes" or Question7 == "yeah"):
  print("Thank you so much I enjoyed talking to you too! Have a nice day!")
elif(Question7 == "no" or Question7 == "nope"):
  print("Oh well I am sorry to hear that...well thank you for letting me interview hope you have a nice day!")




if __name__ == "__main__":
  main()
  t = input("Run pytest? (y/n)").lower()
  if t == 'y':
    run_tests()