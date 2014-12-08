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

responses = {}
def main():
  print "Welcome to the Smelly Squid! Answer a few yes (y) or no (n) questions and I'll mix yer a drink that'll give yer land legs.\n"

  for k,v in questions.items():
    response = str(raw_input(v + ": ")).lower()
    if  response == "y" or response == "yes":
      responses[k] = True
    elif response == "n" or response == "no":
      responses[k] = False
    else:
      # TO-DO allow the question to be repeated if the user enters incorrect details
      print "Errr, yer already drunk, I can't understand yer. Next question."

  return responses

drink = []
def mix_drink(style):
  for k,v in style.items():
    if ingredients.has_key(k) and v == True:
      drink.append(random.choice(ingredients[k]))

  return drink

if __name__ == '__main__':
  main()
  mix_drink(responses)
  print "\nOy, yer drink is ready with the following custom mix: "
  #List the ingredients
  for ingredient in drink:
    print "{}".format(ingredient)