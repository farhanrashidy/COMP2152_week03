import random

# Dice options using list() and range()
diceOptions = list(range(1, 7))

# Weapons array
weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']

print("Available Weapons:", ', '.join(weapons))

# User inputs 
combatStrength = int(input("Enter your combat strength (1-6): "))
if combatStrength < 1 or combatStrength > 6:
    print("Invalid Input! Please enter number from (1-6)")

    # Default value for invalid input
    combatStrength = 1

# input combat strength for Monster
monsterCombatStrength = int(input("Enter monster's combat stength (1-6)"))
if monsterCombatStrength < 1 or monsterCombatStrength > 6:
    print("Invalid Input! Please enter number from (1-6)")

    # Default value for invalid input
    monsterCombatStrength = 1


combatStrength = max(1, min(6, int(input("Hero strength (1-6): "))))
mCombatStrength = max(1, min(6, int(input("Monster strength (1-6): "))))

# Battle
for j in range(1, 21, 2):
    heroRoll, monsterRoll = random.choice(diceOptions), random.choice(diceOptions)
    heroTotal, monsterTotal = combatStrength + heroRoll, mCombatStrength + monsterRoll
    print(f"Round {j}: Hero({weapons[heroRoll - 1]})={heroTotal}, Monster({weapons[monsterRoll - 1]})={monsterTotal}.", 
          "Hero wins!" if heroTotal > monsterTotal else "Monster wins!" if heroTotal < monsterTotal else "Tie!")
    if j == 11:
        print("Battle Truce declared. Game Over!")
        break