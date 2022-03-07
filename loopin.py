alchemist = ['Flame','Fullmetal','Crimson']
for x in alchemist:
    print(x)
    if x == 'Fullmetal':
     break

for x in 'flame':
 print(x)

alchemist = ['Flame','Fullmetal','Crimson']
for name in alchemist:
    print(f'alchemist name is {name}')
#while
i = 7
while i > 1  :
    print('My favourite character is Flame')
    i-=1

#Dictionary is iterable 
me={
    'name':'Orhun',
    'age':18,
    'can_drive':False,
}

for y in me.items():
    print(y)
for y in me.keys(): 
    print(y)