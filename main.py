from art import logo
from replit import clear
from random import choice

continue_asking = True
lines = []
  
while continue_asking:
  print(logo)
  suggestion = input("Please type a funny line that you'd like us to say: ")
  lines.append(suggestion)
  more_lines = input("More lines?: (y / n) ")
  if more_lines == "n":
    continue_asking = False
    print(choice(lines))
  else:
    clear()
