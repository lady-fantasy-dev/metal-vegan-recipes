import random

pairings =[
  {"dish": "Brutal Chickpea Curry", "band": "Behemoth"},
  {"dish": "Crushing Black Bean Tacos", "band": "Cannibal Corpse"},
  {"dish": "Dark & Grim Lentil Tacos", "band": "Katatonia"},
  {"dish": "Extreme Cauliflower Wings", "band": "Dark Funeral"}
]

pairing = random.choice(pairings)

def show_pairing(pairing):
  print("Tonight's metal vegan dish is", pairing["dish"], "paired well with", pairing["band"], "🤘🔥")

show_pairing(pairing)

while True:
  user_input = input("Do you want another random recipe? Enter y or n: ")
  pairing = random.choice(pairings)

  if user_input.lower() == "y":
    show_pairing(pairing)
  elif user_input.lower() == "n":
    print("Okay, goodbye!")
    break
  else:
    print("Error! Try again...")
