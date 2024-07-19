import random, os, time

def rollDice(side):
  result = random.randint(1,side)
  return result

def health():
  healthStat = ((rollDice(6)*rollDice(12))/2)+10
  return healthStat

def strength():
  strengthStat = ((rollDice(6)*rollDice(8))/2)+12
  return strengthStat

print("Character builder")
print()
p1name = input("Name your Character:\n")
p1type = input("Character Type (Human, Elf, Wizard, Orc):\n")
print()
print(p1name)
p1Health = health()
p1Strength = strength()
print("HEALTH:", p1Health)
print("STRENGTH:", p1Strength)
print()
print("Who are you battling?")
print()
p2name = input("Name your Character:\n")
p2type = input("Character Type (Human, Elf, Wizard, Orc):\n")
print()
print(p2name)
p2Health = health()
p2Strength = strength()
print("HEALTH:", p2Health)
print("STRENGTH:", p2Strength)
print()
round = 1
winner = None

while True:
time.sleep(1)
os.system("clear")
print("Battle time")
p1Dice = rollDice(6)
p2Dice = rollDice(6)

difference = abs(p1Strength - p2Strength)+ 1

if p1Dice > p2Dice:
  p2Health -= difference
  if round == 1:
    print(p1Name, "wins round 1")
  else:
    print(p1Name "wins at round", round)
elif p2Dice > p1Dice:
  p2Health -= difference
    if round == 1:
      print(p2Name, "wins at round 1!")
    else:
      print(p2Name,"wins at round", round)
else:
  print("They have a draw at round", round)

  print()
  print(p1Name)
  print("HEALTH:", p1Health)
  print()
  print(p2Name)
  print("HEALTH:", p2Health)

if p1Health <= 0:
  print(p1Name, "has died!")
  winner = p2Name
  break
elif p2Health <= 0:
  print(p2Name, "has died!")
  winner = p1Name
  break
else:
  print("They both lived that round!")
  round += 1
time.sleep(1)
os.system("clear")
print("⚔️ BATTLE TIME ⚔️")
print()
print(winner, "has won on round",round)
