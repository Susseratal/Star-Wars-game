import random
import time
from colorama import Fore

print("Choose your armour:")
print("1: Jedi Robes - high dodge but no defence")
print("2: Commando armour - low dodge but high defence")
print("3: Arc Armour - medium dodge and medium defence")
armour = input("1, 2 or 3: ")
time.sleep(0.5)

print("Choose your weapon:")
print("1: Lightsaber - hightened chance to miss but fairly high damage range and a chance for a second attack")
print("2: Dual DC-17s - allows two attacks with lower damage and regular chance to miss")
print("3: DLT-19x - Highest damage range with regular chance to miss")
weapon = input("1, 2 or 3: ")

swing2 = [1,2,3,4]
miss = [1,2,3]
arcreduce = [1,2,3]
comreduce = [1,2,3,4,5,6,7]
jedodge = [1,2,3,4]
comdodge = [1,2,3,4,5,6,7,8]
arcdodge = [1,2,3,4,5,6]

def battle():
  enemychoice = ['1','2','3']
  time.sleep(0.5)
  enemy = random.choice(enemychoice)
  if enemy == '1':
        print("your enemy is a dark jedi")
  elif enemy == '2':
    print("You enemy is a clanker with Arc level defence and dodge ability and weapons with the same ability as the DC-17s")
  elif enemy == '3':
    print("You enemy is a clanker with commando level defence and dodge ability and weapons with the same ability as a DLT-19x")
  if weapon == "1":
    damage = [10,11,12,13,14]
  if weapon == "2":
    damage = [3,4,5,6,7,8,9]
  if weapon == "3":
    damage = [7,8,9,10,11,12,13,14,15,16]
  if weapon == "1":
    damage = [10,11,12,13,14]
  if weapon == "2":
    damage = [3,4,5,6,7,8,9]
  if weapon == "3":
    damage = [7,8,9,10,11,12,13,14,15,16]
  health = 100
  enemyhealth = 100
  while enemyhealth >= 1:
    if health <= 0:
        print("You are dead")
        exit()
    health = str(health)
    time.sleep(0.5)
    enemyhealth = str(enemyhealth)
    print(Fore.GREEN)
    print("Your health is " + health)
    print("your enemy's health is " + enemyhealth)
    print('would you like to:')
    print("1: Attack")
    print("2: Heal")

    fight = input("1 or 2")
    health = int(health)
    enemyhealth = int(enemyhealth)
    fight = int(fight)
    responses = [1,"1"]
    responses2 = [2,"2"]
    responses3 = [3,"3"]

    if fight in responses:
        time.sleep(0.5)
        print(Fore.BLUE)
        if weapon in responses:
            lmiss = random.choice(miss)
            #print(lmiss)
            if lmiss in responses2:
                go2 = random.choice(swing2)
                hit = random.choice(damage)
                if enemy in responses:
                    avoid = random.choice(jedodge)
                    if avoid in responses:
                        print("Your enemy dodges")
                    else:
                        hit = str(hit)
                        print("Your enemy takes " + hit + " damage")
                        hit=int(hit)
                        enemyhealth = enemyhealth - hit
                elif enemy in responses2:
                    block = random.choice(arcreduce)
                    if block >= hit:
                        hit = 0
                    else:
                        hit = hit - block
                    avoid = random.choice(arcdodge)
                    if avoid in responses:
                        print("Your enemy dodges")
                    else:
                        hit = str(hit)
                        print("Your enemy takes " + hit + " damage")
                        hit=int(hit)
                        enemyhealth = enemyhealth - hit
                elif enemy in responses3:
                    avoid = random.choice(comdodge)
                    block = random.choice(comreduce)
                    if block >= hit:
                        hit = 0
                    else:
                        hit = hit - block
                    if avoid in responses:
                        print("Your enemy dodges")
                    else:
                        hit = str(hit)
                        print("Your enemy takes " + hit + " damage")
                        hit=int(hit)
                        enemyhealth = enemyhealth - hit
                #print(go2)
                if go2 in responses2:
                    time.sleep(0.5)
                    hit == random.choice(damage)
                    if enemy == '1':
                        avoid = random.choice(jedodge)
                        if avoid in responses:
                            print("Your enemy dodges your second attack")
                        else:
                            hit = str(hit)
                            print("Your enemy takes " + hit + " damage from the second shot")
                            hit = int(hit)
                            enemyhealth = enemyhealth - hit
                    elif enemy == '2':
                        block = random.choice(arcreduce)
                        if block >= hit:
                            hit = 0
                        else:
                            hit = hit - block
                        avoid = random.choice(arcdodge)
                        if avoid in responses:
                            print("Your enemy dodges your second attack")
                        else:
                            hit = str(hit)
                            print("Your enemy takes " + hit + " damage from the second shot")
                            hit=int(hit)
                        enemyhealth = enemyhealth - hit
                    elif enemy == '3':
                        avoid = random.choice(comdodge)
                        block = random.choice(comreduce)
                        if block >= hit:
                            hit = 0
                        else:
                            hit = hit - block
                        if avoid in responses:
                            print("Your enemy dodges your second attack")
                        else:
                            hit = str(hit)
                            print("Your enemy takes " + hit + " damage from the second shot")
                            hit=int(hit)
                        enemyhealth = enemyhealth - hit

            else:
                print("You miss")
        elif weapon in responses2:
            lmiss = random.choice(miss)
            #print(lmiss)
            if lmiss not in responses2:
                go2 = random.choice(swing2)
                hit = random.choice(damage)
                if enemy in responses:
                    avoid = random.choice(jedodge)
                    if avoid in responses:
                        print("Your enemy dodges")
                    else:
                        hit = str(hit)
                        print("Your enemy takes " + hit + " damage")
                        hit=int(hit)
                        enemyhealth = enemyhealth - hit
                elif enemy in responses2:
                    block = random.choice(arcreduce)
                    if block >= hit:
                        hit = 0
                    else:
                        hit = hit - block
                    avoid = random.choice(arcdodge)
                    if avoid in responses:
                        print("Your enemy dodges")
                    else:
                        hit = str(hit)
                        print("Your enemy takes " + hit + " damage")
                        hit=int(hit)
                        enemyhealth = enemyhealth - hit
                elif enemy in responses3:
                    avoid = random.choice(comdodge)
                    block = random.choice(comreduce)
                    if block >= hit:
                        hit = 0
                    else:
                        hit = hit - block
                    if avoid in responses:
                        print("Your enemy dodges")
                    else:
                        hit = str(hit)
                        print("Your enemy takes " + hit + " damage")
                        hit=int(hit)
                        enemyhealth = enemyhealth - hit
            else:
              print('You miss')
            lmiss = random.choice(miss)
            #print(lmiss)
            if lmiss not in responses2:
                time.sleep(0.5)
                go2 = random.choice(swing2)
                hit = random.choice(damage)
                if enemy in responses:
                    avoid = random.choice(jedodge)
                    if avoid in responses:
                        print("Your enemy dodges your second attack")
                    else:
                        hit = str(hit)
                        print("Your enemy takes " + hit + " damage from the second shot")
                        hit=int(hit)
                        enemyhealth = enemyhealth - hit
                elif enemy in responses2:
                    block = random.choice(arcreduce)
                    if block >= hit:
                        hit = 0
                    else:
                        hit = hit - block
                    avoid = random.choice(arcdodge)
                    if avoid in responses:
                        print("Your enemy dodges your second attack")
                    else:
                        hit = str(hit)
                        print("Your enemy takes " + hit + " damage from the second shot")
                        hit=int(hit)
                        enemyhealth = enemyhealth - hit
                elif enemy in responses3:
                    avoid = random.choice(comdodge)
                    block = random.choice(comreduce)
                    if block >= hit:
                        hit = 0
                    else:
                        hit = hit - block
                    if avoid in responses:
                        print("Your enemy dodges your second attack")
                    else:
                        hit = str(hit)
                        print("Your enemy takes " + hit + " damage from the second shot")
                        hit=int(hit)
                        enemyhealth = enemyhealth - hit
            else:
              print('You miss with your second shot')
        elif weapon in responses3:
            lmiss = random.choice(miss)
            #print(lmiss)
            if lmiss not in responses2:
                go2 = random.choice(swing2)
                hit = random.choice(damage)
                if enemy in responses:
                    avoid = random.choice(jedodge)
                    if avoid in responses:
                        print("Your enemy dodges")
                    else:
                        hit = str(hit)
                        print("Your enemy takes " + hit + " damage")
                        hit=int(hit)
                        enemyhealth = enemyhealth - hit
                elif enemy in responses2:
                    block = random.choice(arcreduce)
                    if block >= hit:
                        hit = 0
                    else:
                        hit = hit - block
                    avoid = random.choice(arcdodge)
                    if avoid in responses:
                        print("Your enemy dodges")
                    else:
                        hit = str(hit)
                        print("Your enemy takes " + hit + " damage")
                        hit=int(hit)
                        enemyhealth = enemyhealth - hit
                elif enemy in responses3:
                    avoid = random.choice(comdodge)
                    block = random.choice(comreduce)
                    if block >= hit:
                        hit = 0
                    else:
                        hit = hit - block
                    if avoid in responses:
                        print("Your enemy dodges")
                    else:
                        hit = str(hit)
                        print("Your enemy takes " + hit + " damage")
                        hit=int(hit)
                        enemyhealth = enemyhealth - hit
            else:
              print('You miss')
            
    if fight == '2':
      time.sleep(0.5)
      print(Fore.BLUE)
      dam = random.randint(1, 8)
      health = health + dam
      dam = str(dam)
      print("You gain " + dam + " health")
    
    choices = ['attack', 'heal']
    enemyattack = random.choice(choices)
    print(Fore.RED)
    if enemyattack == 'attack':
      time.sleep(0.5)
      if enemy in responses:
            lmiss = random.choice(miss)
            #print(lmissprint(lmiss)
            if lmiss in responses2:
                go2 = random.choice(swing2)
                hit = random.choice(damage)
                if armour in responses:
                    avoid = random.choice(jedodge)
                    if avoid in responses:
                        print("You dodge")
                    else:
                        hit = str(hit)
                        print("You take " + hit + " damage")
                        hit=int(hit)
                        health = health - hit
                elif armour in responses3:
                    block = random.choice(arcreduce)
                    if block >= hit:
                        hit = 0
                    else:
                        hit = hit - block
                    avoid = random.choice(arcdodge)
                    if avoid in responses:
                        print("You dodge")
                    else:
                        hit = str(hit)
                        print("You take " + hit + " damage")
                        hit=int(hit)
                        health = health - hit
                elif armour in responses2:
                    avoid = random.choice(comdodge)
                    block = random.choice(comreduce)
                    if block >= hit:
                        hit = 0
                    else:
                        hit = hit - block
                    if avoid in responses:
                        print("You dodge")
                    else:
                        hit = str(hit)
                        print("You take " + hit + " damage")
                        hit=int(hit)
                        health = health - hit
                time.sleep(0.5)
                if go2 in responses2:
                    hit == random.choice(damage)
                    if armour == '1':
                        avoid = random.choice(jedodge)
                        if avoid in responses:
                            print("You dodge the second attack")
                        else:
                            hit = str(hit)
                            print("You take " + hit + " damage from the second shot")
                            hit = int(hit)
                            health = health - hit
                    elif armour == '3':
                        block = random.choice(arcreduce)
                        if block >= hit:
                            hit = 0
                        else:
                            hit = hit - block
                        avoid = random.choice(arcdodge)
                        if avoid in responses:
                            print("You dodge the second attack")
                        else:
                            hit = str(hit)
                            print("You take " + hit + " damage from the second shot")
                            hit=int(hit)
                        health = health - hit
                    elif armour == '2':
                        avoid = random.choice(comdodge)
                        block = random.choice(comreduce)
                        if block >= hit:
                            hit = 0
                        else:
                            hit = hit - block
                        if avoid in responses:
                            print("You dodge the second attack")
                        else:
                            hit = str(hit)
                            print("You take " + hit + " damage from the second shot")
                            hit=int(hit)
                        health = health - hit

            else:
                print("Your enemy misses")
      elif enemy in responses2:
          lmiss = random.choice(miss)
          #print(lmiss)
          if lmiss not in responses2:
                go2 = random.choice(swing2)
                hit = random.choice(damage)
                if enemy == 1:
                    avoid = random.choice(jedodge)
                    if avoid in responses:
                        print("You dodge")
                    else:
                        hit = str(hit)
                        print("You take " + hit + " damage")
                        hit=int(hit)
                        health = health - hit
                elif enemy in responses2:
                    block = random.choice(arcreduce)
                    if block >= hit:
                        hit = 0
                    else:
                        hit = hit - block
                    avoid = random.choice(arcdodge)
                    if avoid in responses:
                        print("You dodge")
                    else:
                        hit = str(hit)
                        print("You take " + hit + " damage")
                        hit=int(hit)
                        health = health - hit
                elif enemy in responses3:
                    avoid = random.choice(comdodge)
                    block = random.choice(comreduce)
                    if block >= hit:
                        hit = 0
                    else:
                        hit = hit - block
                    if avoid in responses:
                        print("You dodge")
                    else:
                        hit = str(hit)
                        print("You take " + hit + " damage")
                        hit=int(hit)
                        health = health - hit
          else:
              print('Your enemy misses')
          lmiss = random.choice(miss)
          #print(lmiss)
          time.sleep(0.5)
          if lmiss not in responses2:
                go2 = random.choice(swing2)
                hit = random.choice(damage)
                if enemy in responses:
                    avoid = random.choice(jedodge)
                    if avoid in responses:
                        print("You dodge the second attack")
                    else:
                        hit = str(hit)
                        print("You take " + hit + " damage from the second shot")
                        hit=int(hit)
                        health = health - hit
                elif enemy in responses2:
                    block = random.choice(arcreduce)
                    if block >= hit:
                        hit = 0
                    else:
                        hit = hit - block
                    avoid = random.choice(arcdodge)
                    if avoid in responses:
                        print("You dodge the second attack")
                    else:
                        hit = str(hit)
                        print("You take " + hit + " damage from the second shot")
                        hit=int(hit)
                        health = health - hit
                elif enemy in responses3:
                    avoid = random.choice(comdodge)
                    block = random.choice(comreduce)
                    if block >= hit:
                        hit = 0
                    else:
                        hit = hit - block
                    if avoid in responses:
                        print("You dodge the second attack")
                    else:
                        hit = str(hit)
                        print("You take " + hit + " damage from the second shot")
                        hit=int(hit)
                        health = health - hit
          else:
              print('Your enemy misses you with their second shot')
        
      elif enemy in responses3:
            lmiss = random.choice(miss)
            #print(lmiss)
            if lmiss not in responses2:
                go2 = random.choice(swing2)
                hit = random.choice(damage)
                if enemy in responses:
                    avoid = random.choice(jedodge)
                    if avoid in responses:
                        print("You dodge")
                    else:
                        hit = str(hit)
                        print("You take " + hit + " damage")
                        hit=int(hit)
                        health = health - hit
                elif enemy in responses2:
                    block = random.choice(arcreduce)
                    if block >= hit:
                        hit = 0
                    else:
                        hit = hit - block
                    avoid = random.choice(arcdodge)
                    if avoid in responses:
                        print("You dodge")
                    else:
                        hit = str(hit)
                        print("You take " + hit + " damage")
                        hit=int(hit)
                        health = health - hit
                elif enemy in responses3:
                    avoid = random.choice(comdodge)
                    block = random.choice(comreduce)
                    if block >= hit:
                        hit = 0
                    else:
                        hit = hit - block
                    if avoid in responses:
                        print("You dodge")
                    else:
                        hit = str(hit)
                        print("You take " + hit + " damage")
                        hit=int(hit)
                        health = health - hit
            else:
              print('Your enemy misses')
    if enemyattack == 'heal':
      time.sleep(0.5)
      dam = random.randint(1, 5)
      enemyhealth = enemyhealth + dam
      dam = str(dam)
      print("Your enemy gains " + dam + " health")

  print("Before you your enemy lies dead and defeated")

battle()
