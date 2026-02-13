import random


def rotate_dice():
    """
    DOCSTRING!!!
    This function simulates a simple dice game.
    First, two dice are rolled.
      If the total is 7 or 11, the player wins.
      If the total is 2, 3, or 12 the casino wins.
      Otherwise that total becomes the goal number.

    Then the dice keep rolling until:
      The player rolls the goal number again (player wins) or
      The player rolls a 7 (casino wins).
    """
    numbers = [1, 2, 3, 4, 5, 6]

    dice_1 = random.choice(numbers)
    dice_2 = random.choice(numbers)
    total = dice_1 + dice_2
    print(f"First roll: {dice_1} + {dice_2} = {total}")

    if total in [7, 11]:
        print("Player Wins")
    elif total in [2, 3, 12]:
        print("Casino wins")
    else:
        goal = total
        print(f"Now your goal number is {goal}")


        while True:

            new_d1 = random.choice(numbers)
            new_d2 = random.choice(numbers)
            new_total = new_d1 + new_d2
            print(f"Rolled: {new_total}")

            if new_total == goal:
                print("You hit your goal! Player Wins")
                break
            elif new_total == 7:
                print("You rolled a 7! Casino wins")
                break


rotate_dice()