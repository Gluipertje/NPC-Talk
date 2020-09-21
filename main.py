import random

inputMeaning = []
userInput = []

def getInput():
  userInput = input("You: ").lower().split()
  getWordMeaning(userInput)
  
def getWordMeaning(Ainput):
  for i in range(len(Ainput)):
    if Ainput[i] == "hello" or Ainput[i] == "hey" or Ainput[i] == "hi" or Ainput[i] == "ey" or Ainput[i] == "aye":
      inputMeaning.append("GREETING")
    elif Ainput[i] == "fuck" or Ainput[i] == "gay" or Ainput[i] == "kanker" or Ainput[i] == "tering" or Ainput[i] == "kut":
      inputMeaning.append("SWEAR")
    elif Ainput[i] != "":
      inputMeaning.append("FILLER")
  react()

def react():
  for i in range(len(inputMeaning)):
    randN = random.randint(0, 3)
    if inputMeaning[i] == "GREETING":
      if randN == 1:
        respond("Hey")
      else:
        respond("Hoi")
    elif inputMeaning[i] == "SWEAR":
      if randN == 1:
        respond("haha lol")
      elif randN == 2:
        respond("haha kom dan")
      else:
        respond("ja")
  inputMeaning.clear()
  getInput()
        
def respond(response):
  print("Bot: " + response)

getInput()
