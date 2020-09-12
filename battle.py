import random

def battle():
    while True:
        print ("Do you want to: ")
        print ("1: Attack")
        print ("2: Block")
        print ("3: Use item")
        act = input ("")
        act = act.lower()
        if act == "attack":
            crit = random.randint(1,100)
            dmg = random.randint(18, 30)
            if crit == 23:
                dmg == ("100")
                print ("CRITICAL HIT! You do 100 damage")
            else:
                print ("You do " + dmg + " damage")

        elif act == "defend":

