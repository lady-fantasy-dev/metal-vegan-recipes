import random

metalrecipes = ["Brutal Chickpea Curry", "Crushing Black Bean Tacos", "Dark & Grim Lentil Tacos"]

print("Today's metal vegan recipe is", random.choice(metalrecipes), "🤘🔥")

while True:
  user_input = input("Do you want another random recipe? Enter y or n: ")
  if user_input.lower() == "y":
    print("Your next metal vegan recipe is", random.choice(metalrecipes), "🤘🔥")
  elif user_input.lower() == "n":
    print("Okay, goodbye!")
    break
  else:
    print("Error! Try again...")
