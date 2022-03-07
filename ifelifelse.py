a = 84
b = 56
if b>a :
    print('b greater than a')
elif b == a : 
    print('a and b are equal')
else :
    print('a greater than b')

x = 0 
y = 3
if x < y :
    print('x is greater than y')
else : 
    print('x is not greater than y')

d = 4
ı = 7
u = 13
if d<ı and u>ı :
    print('both are conditions are true')

if a > 10: 
    print('Above ten,') 
    if a > 30 :
      print('and also above 30!')
    else : 
        print('but not above 90') 
#Weapon choice
selectionStr = 'Enter your weapon choice:\n1-sword\n2-arrow\n3-shield\n'

weapon = int(input(selectionStr))
if weapon == 1 :
    print('Your weapon is Melee Attack and your character is mainly violent')
elif weapon == 2 :
    print('Your weapon is Ranged and Tactical and your character is smart and cold-blooded')
elif weapon == 3 :
    print('Your weapon is Defence and your character is mainly defence')
else : 
     print('Weapon not selected')


