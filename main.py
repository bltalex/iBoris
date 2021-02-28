"""
Hackathon Project for WarwickHACK 2021

"""
from data import *
from speech import sound
from UI import MainApp

def threatlevel(cases,percentchange):
  if cases < 400:
    threatlevel = 1
  elif cases < 1200:
    threatlevel = 2
  elif cases < 5000:
    threatlevel = 3
  elif cases < 15000:
    threatlevel = 4
  else:
    threatlevel = 5

  if percentchange > 0.15:
    threatlevel += 2
  elif percentchange > 0.05:
    threatlevel += 1
  elif percentchange < -0.15:
    threatlevel -= 2
  elif percentchange < -0.5:
    threatlevel -= 1

  if threatlevel > 5:
    threatlevel = 5
  elif threatlevel < 1:
    threatlevel = 1

  return threatlevel

a = get_new_cases()
b = percent_change()
TL = threatlevel(a,b)

#try sound(TL)
app = MainApp()
app.set_threatlevel(TL)
app.run()