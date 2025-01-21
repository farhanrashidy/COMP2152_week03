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
monsterCombatStrength = max(1, min(6, int(input("Monster strength (1-6): "))))

# Simulate Battle Round
for j in range(1, 21, 2):  #Simulate for 20 rounds, steppign by 2

    # Dice roll for hero and monster 
    heroRoll =random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    # Calculate weapon selected
    heroWeapon = weapons[heroRoll - 1]
    monsterWeapon = weapons[monsterRoll - 1]

    # Calculate total strength
    heroTotal = combatStrength + heroRoll
    monsterTotal = monsterCombatStrength + monsterRoll

    # Print round details
    print(f"\nRound {j} Hero rolled {heroRoll}, Monster rolled {monsterRoll}")
    print(f"\nHero selected: {heroWeapon}, Monster selected: {monsterWeapon} ")
    print(f"Hero total strength: {heroRoll}, Monster total strength: {monsterTotal}")

    # Determine winner
    if heroTotal > monsterTotal:
        print("Hero wins the round!")
    elif heroTotal < monsterTotal:
        print("Monster wins the round")
    else: print("It's a tie!")

    if j == 11:
        print("\n Batte Truce declared in Round 11. Game Over!")
        break
if j != 11:
    print("\n Battle concluded after 20 rounds!")