from random import randint
import os
import platform


def openLink(a,b,x1,x2,x3,x4):

  system = platform.system()

  openType = "start" if system == "Windows" else "xdg-open" 

  string = "{} https://prnt.sc/{}{}{}{}{}{}".format(openType,a,b,x1,x2,x3,x4)
  os.system(string)


for i in range(int(input("How many random images do you want to see?"))):
  x1 = randint(0,9)
  x2 = randint(0,9)
  x3 = randint(0,9)
  x4 = randint(0,9)
  a = chr(randint(97,122))
  b = chr(randint(97,122))
  openLink(a,b,x1,x2,x3,x4)
  #print(string)
