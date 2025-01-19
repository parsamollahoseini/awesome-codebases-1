import random

# Define an array of weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

# Roll the dice (1-6) to choose a weapon
try:
    # Simulate rolling a dice (1-6)
    weaponRoll = random.randint(1, 6)
    print(f"You rolled a {weaponRoll}.")

    # Add weaponRoll to hero's combat strength (assuming heroCombatStrength is defined elsewhere)
    heroCombatStrength = 10  # Example combat strength
    heroCombatStrength += weaponRoll

    # Use weaponRoll as an index into the weapons array
    heroWeapon = weapons[weaponRoll - 1]  # -1 because lists are 0-indexed
    print(f"The hero's weapon is: {heroWeapon}")

    # Define the condition based on weaponRoll
    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend.")
    elif weaponRoll <= 4:
        print("Your weapon is meh.")
    else:
        print("Nice weapon, friend!")

    # Check if the weapon rolled is not a Fist
    if heroWeapon != "Fist":
        print("Thank goodness you didn't roll the Fist...")
    else:
        print("Uh-oh, you're stuck with a Fist!")

except ValueError as e:
    print(f"Error: Invalid input detected. {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
