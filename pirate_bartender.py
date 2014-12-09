import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def main():
  responses = {}
  "Welcome to the Smelly Squid! How would yer like yer drink? "

  for flavour,question in questions.items():
    response = str(raw_input(question + ": ")).lower()
    if  response == "y" or response == "yes":
      responses[flavour] = True
    elif response == "n" or response == "no":
      responses[flavour] = False
    else:
      # TO-DO allow the question to be repeated if the user enters incorrect details
      print "Errr, yer already drunk, I can't understand yer. Next question."

  return responses

def mix_drink(style):
  drink = []
  for flavour,ingredient in style.items():
    if ingredients.has_key(flavour) and ingredient == True:
      drink.append(random.choice(ingredients[flavour]))

  return drink

if __name__ == '__main__':
  responses = main()
  drink = mix_drink(responses)
  print "\nOy, yer drink is ready with the following custom mix: "
  #List the ingredients
  for ingredient in drink:
    print "- {}".format(ingredient)