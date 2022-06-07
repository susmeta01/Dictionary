import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def meaning(word):
   word = word.lower()
   if word in data:
      return data[word]
   elif word.title() in data:
      return data[word.title()]
   elif word.upper() in data:
      return data[word.upper()]
   elif len(get_close_matches(word,data.keys())) > 0:
      ans = input("Did you mean %s ? Enter Y if yes or N if no : " %get_close_matches(word,data.keys())[0])
      if ans == "Y" or ans == "y":
         return data[get_close_matches(word,data.keys())[0]]
      elif ans == "N" or ans == "n":
         return("Word does not exist. Please double check it")
      else:
         return("We are not able to understand your entry")
   else:
      return("Word does not exist. Please double check it")

word = input("Enter a word: ")

output = meaning(word)
if type(output) == list:
   for items in output:
      print (items)
else:
   print (output)