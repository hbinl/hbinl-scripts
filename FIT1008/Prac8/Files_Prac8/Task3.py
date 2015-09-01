"""
FIT1008 Prac 8 Task 3
Loh Hao Bin 25461257, Tan Wen Jie 25839063
@purpose: gladiatorialCombat
@created 20140923
@modified 20140924
"""

from Task1 import *
from Task2 import *
import time

def gladiatorialCombat(Player1_army, Player2_army):
    """
        @purpose: To simulate a gladiatorial battle
        @complexity:
            Best Case: O(1), when the army input is invalid, no stack
            Worst Case: O(N*M), where n is the number of units in stack, and m is the life of the unit
        @parameter:
            name: Name of the player of this army, if empty, it will ask for input
            inp: Units of the army in S A C format, if empty, it will ask for input
        @precondition: Two Army classes are initialised
        @postcondition: A gladiatorial battle is carried out, either or both army stacks are empty
    """
    empty = False

    round_no = 1

    while not empty:
        # just printing round numbers
        print("_" * 35)
        print("\nRound " + str(round_no))


        # pop the top surviving player from player 1's stack
        p1_current_unit = Player1_army.pop()
        print("\n> Player 1 " + Player1_army.player_name())
        print(p1_current_unit)

        print("vs")

        # pop the top surviving player from player 2's stack
        p2_current_unit = Player2_army.pop()
        print("> Player 2 " + Player2_army.player_name())
        print(p2_current_unit)


        p1_current_unit, p2_current_unit = battle(p1_current_unit, p2_current_unit)

        # post battle check
        if p1_current_unit.isAlive() == True and p2_current_unit.isAlive() == True:
            # if both still alive, -1 from both sides
            # post battle trauma
            p1_current_unit.loseLife(1)
            p2_current_unit.loseLife(1)
            print("Both sides are still standing strong, -1 life from both sides.")

            # check if they are still alive
            if p1_current_unit.isAlive() == True:
                # if yes, push back into stack
                p1_current_unit.gainExperience(1)
                Player1_army.push(p1_current_unit)
            else:
                print("Player 1 lost one unit from post battle trauma!")

            if p2_current_unit.isAlive() == True:
                p2_current_unit.gainExperience(1)
                Player2_army.push(p2_current_unit)
            else:
                print("Player 2 lost one unit from post battle trauma!")
        else:

            # if one of them alive, +1 exp and push back
            if p1_current_unit.isAlive() == True:
                print("Player 1's " + p1_current_unit.unit_name() + " gains 1 experience point.")
                p1_current_unit.gainExperience(1)
                Player1_army.push(p1_current_unit)

            elif p2_current_unit.isAlive() == True:
                print("Player 2's " + p2_current_unit.unit_name() + " gains 1 experience point.")
                p2_current_unit.gainExperience(1)
                Player2_army.push(p2_current_unit)

            else:
                # if none of them alive
                print("Player 1 and 2 lost both their units in this round.")

        # check end game
        empty = check_end_game(Player1_army, Player2_army)

        round_no += 1

        time.sleep(0.1)


def battle(p1_current_unit, p2_current_unit):
    """
            @purpose: To carry out the battle
            @complexity:
                Best & Worst Case: O(1), when the army input is invalid, no stack
            @parameter:
                p1_current_unit: The current unit of p1
                p2_current_unit: The current unit of p2
            @precondition: Two units from both sides are passed
            @postcondition: A gladiatorial battle is carried out, and returns the units after battle
    """
    # Battle is on
    # Compare the unit's speeds
    if p1_current_unit.getSpeed() > p2_current_unit.getSpeed():
            # if u1 > u2 in speed
            # u1 attack first

            atk = p1_current_unit.attack()
            dmg = p2_current_unit.defend(atk)
            print("Player 1's " + p1_current_unit.unit_name() + " attacks for " + str(dmg) + " damage!")

            # after attacking, check if u2 still alive
            # if yes, u2 retaliates
            if p2_current_unit.isAlive() == True:

                atk = p2_current_unit.attack()
                dmg = p1_current_unit.defend(atk)
                print("Still standing, Player 2's " + p2_current_unit.unit_name() + " attacks for " + str(dmg) + " damage!")

                # check if u2's attack killed u1
                if p1_current_unit.isAlive() == False:
                    print("Player 1 lost one unit!")
            else:
                # if no, u2 dead
                print("Player 2 lost one unit!")

    # if u1 < u2 in speed
    # u2 attack first
    elif p1_current_unit.getSpeed() < p2_current_unit.getSpeed():
            atk = p2_current_unit.attack()
            dmg = p1_current_unit.defend(atk)
            print("Player 2's " + p2_current_unit.unit_name() + " attacks for " + str(dmg) + " damage!")

            # check if u1 still alive
            # if yes, u1 retaliates
            if p1_current_unit.isAlive() == True:
                atk = p1_current_unit.attack()
                dmg = p2_current_unit.defend(atk)
                print("Still standing, Player 1's " + p1_current_unit.unit_name() + " attacks for " + str(dmg) + " damage!")

                # check if u1's retaliation killed u2
                if p2_current_unit.isAlive() == False:
                    print("Player 2 lost one unit!")
            else:
                print("Player 1 lost one unit!")

    else:
            # equal speed
            print("Player 1's " + p1_current_unit.unit_name() + " and 2's " + p2_current_unit.unit_name() + " attacks!")
            atk1 = p1_current_unit.attack()
            atk2 = p2_current_unit.attack()
            dmg1 = p2_current_unit.defend(atk1)
            print("Player 2 receive " + str(dmg1) + " damage!")
            dmg2 = p1_current_unit.defend(atk2)
            print("Player 1 receive " + str(dmg2) + " damage!")
            if p2_current_unit.isAlive() == False:
                    print("Player 2 lost one unit!")
            if p1_current_unit.isAlive() == False:
                    print("Player 1 lost one unit!")

    # return the units post battle
    return p1_current_unit, p2_current_unit

def check_end_game(Player1_army, Player2_army):
    """
        @purpose: To check if the game ends by checking whether any of their army are empty
        @complexity: Best & Worst: O(1)
        @parameter:
            Player1_army: The army of player 1
            Player2_army: The army of player 2
        @precondition: Two Army classes are initialised
        @postcondition: Return True or False depending whether any of the player's stacks are empty
    """
    if Player1_army.is_empty() == True and Player2_army.is_empty() == True:
            print()
            print("*" * 35)
            print("Both armies does not have any units left. It's a DRAW!")
            return True
    elif Player1_army.is_empty() == True:
            print()
            print("*" * 35)
            print("Player 2 Wins! \nRemaining units in army:")
            print(Player2_army)
            return True
    elif Player2_army.is_empty() == True:
            print()
            print("*" * 35)
            print("Player 1 Wins! \nRemaining units in army:")
            print(Player1_army)
            return True
    else:
            # if both players still have units alive
            return False


def battle_test_case():
    print("Testing valid input")
    p1 = Army("Wen Jie", "1 2 3")
    p2 = Army("Hao Bin", "2 2 4")
    gladiatorialCombat(p1, p2)

    print()
    print("*" * 35)
    print("Testing equal input")
    p1 = Army("Wen Jie", "1 2 3")
    p2 = Army("Hao Bin", "1 2 3")
    gladiatorialCombat(p1, p2)

    print()
    print("*" * 35)
    print("Testing invalid input")
    p1 = Army("Wen Jie", "1 1 1 1")
    p2 = Army("Hao Bin", "2 2 a")
    gladiatorialCombat(p1, p2)



def battle_test_menu():
    print("Welcome to the Clans of Clash! ")
    print("\nPlayer 1")
    p1 = Army()
    print("\nPlayer 2")
    p2 = Army()
    gladiatorialCombat(p1, p2)


if __name__ == "__main__":
    try:
        #battle_test_case()
        battle_test_menu()
    except KeyboardInterrupt:
        print("User stopped the program.")
