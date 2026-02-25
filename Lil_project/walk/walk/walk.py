import random as r
#variables
boss_win = False
we_win = False
#User
health = 100
crit = 1

def crit():
    #chance for the next attack to deal a multiplied amount of damage
    c = r.randint(1,5)
    if c > 3:
        crit = crit + 1
    else:
        print("Couldn't crit")
def heal():
    global health
    chance = r.randint(0,4)
    amount = r.randint(25,75)
    if chance > 2:
        health = health + amount
        print(f"you healed {amount} points, and now you have {health} health")
    else:
        print("you didn't heal")
def hit():
    global boss
    global crit
    damage = r.randint(50,100)
    chance = r.randint(1, 100)
    if chance > 33:
        damage = damage * crit
        if crit > 1:
            crit = 1
        boss = boss - damage
        print(f"you dealed {damage} damage, he now has {boss} health")
    else:
        print("you missed")

def user_turn():
    choice = input("enter here: ")
    if choice == "hit" or "h":
        hit()
    elif choice == "block" "b":
        shield = shield + 1
    elif choice == "heal" or "he":
        heal()
    elif choice == "crit" or "c":
        crit()
    elif choice == "2":
        health = 99999
#Boss
boss = 1000

def healb():
    global boss
    chance = r.randint(0,6)
    amount = r.randint(25,75)
    if chance > 2:
        boss = boss + amount
        print(f"The boss healed {amount} amount, and now he has {boss} health")
    else:
        print("he try to heal, but didn't")
def hitb():
    global health
    damage = r.randint(10,30)
    chance = r.randint(1, 100)
    if chance > 20:
        health = health - damage
        print(f"you got {damage} damage, you now have {health} health")
    else:
        print("you dodged his attack")

def boss_turn():
    choice = r.randint(1,2)
    if choice == 1:
        hitb()
    elif choice == 2:
        healb()


#Acutal game
print("Do you want to hit,crit, or heal?")

while we_win == False or boss_win == False:
    user_turn()
    boss_turn()