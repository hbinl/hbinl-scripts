"""
FIT1008 Prac 8 Task 1
Loh Hao Bin 25461257, Tan Wen Jie 25839063
@purpose: Simple Game Classes
@created 20140918
@modified 20140918
"""

class Soldier:
    cost = 1
    speed = 1
    def __init__(self):
        """
        @purpose: To initialise the health and experience
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: None
        @postcondition: Instance of health and experience
        """
        self.life = 3
        self.experience = 0

    def isAlive(self):
        """
        @purpose: To check if character is still alive
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: Instance life
        @postcondition: True/False
        """
        return self.life > 0

    def loseLife(self,lostLife):
        """
        @purpose: To lose character's life
        @complexity:
        Best & Worst Case: O(1)
        @parameter loseLife: Life to lose
        @precondition: Instance life
        @postcondition: Instance life
        """
        self.life -= lostLife

    def gainExperience(self,gainedExperience):
        """
        @purpose: To give character experience
        @complexity:
        Best & Worst Case: O(1)
        @parameter gainedExperience: Experience to gain
        @precondition: Experience instance
        @postcondition: Then new Experience instance
        """
        try:
            int(gainedExperience)
            self.experience += gainedExperience
        except ValueError:
            self.experience += 0

    def getCost(self):
        """
        @purpose: To get the character's cost
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: A static variable cost
        @postcondition: Returns the character's cost
        """
        return self.cost

    def getSpeed(self):
        """
        @purpose: To give character's speed
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: Instance experience
        @postcondition: Returns the character's speed
        """
        return self.speed + self.experience

    def attack(self):
        """
        @purpose: To give character's attack
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: Instance experience
        @postcondition: Returns the character's attacks
        """
        return 1 + self.experience

    def defend(self,damage):
        """
        @purpose: To determine if a character should receive a damage
        @complexity:
        Best & Worst Case: O(1)
        @parameter damage: Damage given to a character
        @precondition: Instance experience, and function loseLife
        @postcondition: Life of the character
        """
        if damage > self.experience:
            self.loseLife(1)
            return 1
        return 0

    def __str__(self):
        """
        @purpose: To print the character's status
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: Instance experience, and life
        @postcondition: Returns the character's status
        """
        string = 'Soldier | HP: ' + str(self.life) + ' | Exp: ' + str(self.experience)
        return string

    def unit_name(self):
        """
        @purpose: To give unit type
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: None
        @postcondition: Returns the type of unit
        """
        return "Soldier"

class Archer:
    cost = 2
    speed = 3
    def __init__(self):
        """
        @purpose: To initialise the health and experience
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: None
        @postcondition: Instance of health and experience
        """
        self.life = 3
        self.experience = 0

    def isAlive(self):
        """
        @purpose: To check if character is still alive
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: Instance life
        @postcondition: True/False
        """
        return self.life > 0

    def loseLife(self,lostLife):
        """
        @purpose: To lose character's life
        @complexity:
        Best & Worst Case: O(1)
        @parameter loseLife: Life to lose
        @precondition: Instance life
        @postcondition: Instance life
        """
        self.life -= lostLife

    def gainExperience(self,gainedExperience):
        """
        @purpose: To give character experience
        @complexity:
        Best & Worst Case: O(1)
        @parameter gainedExperience: Experience to gain
        @precondition: Experience instance
        @postcondition: Then new Experience instance
        """
        try:
            int(gainedExperience)
            self.experience += gainedExperience
        except ValueError:
            self.experience += 0

    def getCost(self):
        """
        @purpose: To get the character's cost
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: A static variable cost
        @postcondition: Returns the character's cost
        """
        return self.cost

    def getSpeed(self):
        """
        @purpose: To give character's speed
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: Instance experience
        @postcondition: Returns the character's speed
        """
        return self.speed

    def attack(self):
        """
        @purpose: To give character's attack
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: Instance experience
        @postcondition: Returns the character's attacks
        """
        return 1 + self.experience

    def defend(self,damage):
        """
        @purpose: To determine if a character should receive a damage
        @complexity:
        Best & Worst Case: O(1)
        @parameter damage: Damage given to a character
        @precondition: Instance experience, and function loseLife
        @postcondition: Life of the character
        """
        self.loseLife(1)
        return 1

    def __str__(self):
        """
        @purpose: To print the character's status
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: Instance experience, and life
        @postcondition: Returns the character's status
        """
        string = 'Archer  | HP: ' + str(self.life) + ' | Exp: ' + str(self.experience)
        return string

    def unit_name(self):
        """
        @purpose: To give unit type
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: None
        @postcondition: Returns the type of unit
        """
        return "Archer"


class Cavalry:
    cost = 3
    speed = 2
    def __init__(self):
        """
        @purpose: To initialise the health and experience
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: None
        @postcondition: Instance of health and experience
        """
        self.life = 4
        self.experience = 0

    def isAlive(self):
        """
        @purpose: To check if character is still alive
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: Instance life
        @postcondition: True/False
        """
        return self.life > 0

    def loseLife(self,lostLife):
        """
        @purpose: To lose character's life
        @complexity:
        Best & Worst Case: O(1)
        @parameter loseLife: Life to lose
        @precondition: Instance life
        @postcondition: Instance life
        """
        self.life -= lostLife

    def gainExperience(self,gainedExperience):
        """
        @purpose: To give character experience
        @complexity:
        Best & Worst Case: O(1)
        @parameter gainedExperience: Experience to gain
        @precondition: Experience, given in integers
        @postcondition: Then new Experience instance
        """
        try:
            int(gainedExperience)
            self.experience += gainedExperience
        except ValueError:
            self.experience += 0

    def getCost(self):
        """
        @purpose: To get the character's cost
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: A static variable cost
        @postcondition: Returns the character's cost
        """
        return self.cost

    def getSpeed(self):
        """
        @purpose: To give character's speed
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: Instance experience
        @postcondition: Returns the character's speed
        """
        return self.speed

    def attack(self):
        """
        @purpose: To give character's attack
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: Instance experience
        @postcondition: Returns the character's attacks
        """
        return 2 * self.experience + 1

    def defend(self,damage):
        """
        @purpose: To determine if a character should receive a damage
        @complexity:
        Best & Worst Case: O(1)
        @parameter damage: Damage given to a character
        @precondition: Instance experience, and function loseLife
        @postcondition: The unit lose life depending on formula
        """
        if damage > (self.experience / 2):
            self.loseLife(1)
            return 1
        return 0

    def __str__(self):
        """
        @purpose: To print the character's status
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: Instance experience, and life
        @postcondition: Returns the character's status
        """
        string = 'Cavalry | HP: ' + str(self.life) + ' | Exp: ' + str(self.experience)
        return string

    def unit_name(self):
        """
        @purpose: To give unit type
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: None
        @postcondition: Returns the type of unit
        """
        return "Cavalry"

def test_menu():
    """
        @purpose: To let the user test all the modules with the desired characters
        @complexity:
        Best & Worst Case: O(1)
        @parameter: None
        @precondition: Class Soldier, Archer, Cavalry
        @postcondition: Returns the respective function's output
        """
    try:
        print("1. Soldier")
        print("2. Archer")
        print("3. Cavalry")
        ans = int(input("Which Character to Test? "))

        if ans == 1:
            unit = Soldier()
        elif ans == 2:
            unit = Archer()
        elif ans == 3:
            unit = Cavalry()
        else:
            raise ValueError

        quit = False

        while not quit:
            print("\n1. isAlive() ")
            print("2. loseLife()")
            print("3. gainExperience()")
            print("4. getCost()")
            print("5. getSpeed()")
            print("6. attack()")
            print("7. defend()")
            print("8. Status")
            print("9. Quit")
            print("10. Test Cases")
            print(str(unit))

            cmd = int(input("Command: "))

            if cmd == 1:
                print("Alive? " + str(unit.isAlive()))
            elif cmd == 2:
                life_lost = int(input("Life Lost: "))
                unit.loseLife(life_lost)
            elif cmd == 3:
                exp = int(input("Experience to gain: "))
                unit.gainExperience(exp)
            elif cmd == 4:
                print(unit.getCost())
            elif cmd == 5:
                print(unit.getSpeed())
            elif cmd == 6:
                print("Attack: " + str(unit.attack()))
            elif cmd == 7:
                dmg = int(input("Damage to receive: "))
                unit.defend(dmg)
            elif cmd == 8:
                print(str(unit))
            elif cmd == 9:
                quit = True
            elif cmd == 10:
                test_function(unit)
                quit = True
            else:
                raise ValueError



    except ValueError:
        print("Please input a valid input.")


def test_function(unit):
    print("\nCost: " + str(unit.getCost()))
    print("Gain 2 experience")
    unit.gainExperience(2)
    print("Gain 'n' experience")
    unit.gainExperience("n")
    print("Speed: " + str(unit.getSpeed()))
    print("Attack: " + str(unit.attack()))
    print(str(unit))
    print("Alive? " + str(unit.isAlive()))
    unit.gainExperience(-1)
    print(str(unit))

    for i in range(3):
        print("Defending 3 damage")
        unit.defend(3)
        print(str(unit))
        print("Alive? " + str(unit.isAlive()))



if __name__ == "__main__":
    try:
        test_menu()
    except KeyboardInterrupt:
        print("User stopped the program.")