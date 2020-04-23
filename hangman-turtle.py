import turtle
import random

word = "test"
# word = input("What's the word?  ")
# for i in range(10):
    # print(".")
print(word)

def drawNoose():
  turtle.color("black")
  turtle.goto(0,0)
  # turtle.forward(120)
  # turtle.forward(-60)
  # turtle.left(90)
  # turtle.forward(150)
  # turtle.right(90)
  # turtle.forward(100)
  # turtle.right(90)
  # turtle.forward(30)
  # turtle.right(90)
  turtle.Screen().exitOnClick()

drawNoose()

def drawHead():
  turtle.circle(15)
  turtle.circle(15, 180) # draw a semicircle
  turtle.right(90)

def drawArms():
  turtle.forward(5)
  turtle.left(90)
  turtle.forward(20)
  turtle.forward(-40)
  turtle.forward(20)
  turtle.right(90)

def drawTorso():
  turtle.forward(30)

def drawLegs():
    turtle.left(45)
    turtle.forward(30)
    turtle.forward(-30)
    turtle.right(90)
    turtle.forward(30)
    turtle.forward(-30)
    turtle.left(45)
    
def startGame(word):
  guessesSoFar = 0
  allowedGuesses = 4  # head, arms, body, legs
  lettersUsedSoFar = []

  answer = "_".join(word) + "_"
  print("The word to guess:  " + " ".join(answer[1:-1:2]))

  guess = ""

  while guessesSoFar < allowedGuesses and answer.find(guess + "_") > -1:
    guess = input("Guess a letter:  ")

    while guess in lettersUsedSoFar:
        guess = input("Please guess a letter you have not used before:  ")

    while len(guess) != 1:
        guess = input("Please only enter one character at a time.  ")

    lettersUsedSoFar.append(guess)

    if guess in word:
        print("Yes, '" + guess + "' is in the word!")
        answer = answer[0:answer.find(guess + "_")+1] + guess + answer[answer.find(guess + "_")+2:]
    
    else:
        guessesSoFar += 1
        print("'" + guess + "' is not in the word.")
        drawHangman(guessesSoFar)

    print("The word to guess:  " + answer[1:-1:2])


# startGame(input("What's the word to guess?  "))