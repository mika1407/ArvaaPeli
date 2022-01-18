import os

# System call
os.system("")

# Class of different styles
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

#from random import randrange
#luku = (randrange(1,21))

from random import randint
luku = randint(1,20)

print("\nTämä on arvaa luku peli. Tervetuloa!")

class style():
  YELLOW = '\033[33m'
print(style.YELLOW + "Arvaa luku väliltä 1...20.")

count = 0
while (count < 3):
  count = count+1
  syöte = input("Anna luku: ")

  if int(syöte) > luku:
    print("Luku on pienempi kuin " + syöte)
  elif int(syöte) < luku:
    print("Luku on suurempi kuin " + syöte)
  else:
    class style():
      RED = '\033[31m'
    print(style.RED + "Arvasit oikein!")
    break

class style():
  WHITE = '\033[37m'
print(style.WHITE + "Oikea luku oli: " + str(luku))

