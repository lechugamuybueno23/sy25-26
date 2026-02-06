import random as r
#variables
boss_win = False
we_win = False
#User
health = 100
shield = 0
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
    damage = r.randint(50,100)
    chance = r.randint(1, 100)
    if chance > 33:
        boss = boss - damage
        print(f"you dealed {damage} damage")
    else:
        print("you missed")
#Boss
boss = 1000
def healb():
    global boss
    chance = r.randint(0,6)
    if chance > 2:
        health = health + 25
        print(f"you healed, and now you have {health} health")
    else:
        print("you didn't heal")
def hitb():
    global health
    damage = r.randint(10,30)
    chance = r.randint(1, 100)
    if chance > 20:
        health = health - damage
        print(f"you got {damage} damage, you now have {health} health")
    else:
        print("you dodged his attack")

print("Do you want to hit,block, or heal?")

while we_win == False or boss_win == False:
    choice = input("enter here: ")
    if choice == "hit":
        hit()
    elif choice == "block":
        shield = shield + 1
    elif choice == "heal":
        heal()
    else:
        print("Next turn")
