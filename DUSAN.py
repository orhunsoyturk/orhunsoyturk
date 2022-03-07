
name = 'Enter your character name:'

character_name = str(input(name)).lower()
print(character_name)

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

char_class = 'Enter your char class:\n4-magic\n5-thief\n6-warrior\n'

classes = int(input(char_class))

if classes == 4:
  print('Your class is mainly magic power its mean can create pot')
elif classes == 5:
    print('Your class is thief its mean your character is speed')
elif classes == 6: 
    print('Your class is warrior its mean your character is strong')
else :
    print('Class not selected')



