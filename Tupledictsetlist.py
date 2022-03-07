     #Booleans 
     
print(7 < 8)
print(9 > 10)
print(8==9)

    #İts simple logic True or False
    #İf else 

ot=7
uy=9

if uy > ot :
    print('uy greater than ot')
else:
    print('uy is not greater than ot')

print(bool('Hello'))
print(bool(ot))
print(bool(''))

def myfunction():
    return 0
print(myfunction())

def myFunction():
    return 0
    
if myFunction():
    print('EVEET!')

else: 
    print('HAYIIR!')
    #Operator
x=7

x+=7
print(x)
     #List mantığı 

cars=['Ferrari','Lamborghini','BMW']
cars.append('Audi')
cars.remove('BMW')
cars.insert(2,'Mercedes')

print(cars)
print(cars[-2])
print(len(cars))
print(type(cars))
print(cars[2:4])

    #Same things
for x in cars:
 print(x)

[print(x) for x in cars]

#Tuple
giray=("Soğukkanklı",4,True)
print(type(giray))
print(giray[0:2])

giray=("Soğukkanlı",4,True)
if "Soğukkanlı" in giray:
 print("Evet var")

giray=("Soğukkanlı",4,True)
y = ("Orhun'un abisi",)
giray +=y
print(giray)
 
giray=("Soğukkanlı",4,True)
(sarı,kırmızı,siyah) = giray

print(sarı)
print(kırmızı)

     #Yaptığım şey hepsine birer karşılık verme
     #SET, aynı şeyi birden fazla kez yazarsan sadece birini alır. Aynı zamanda değişken olabilirler.
kuslar = {"karga","serçe","kuzgun","kartal"} 

print(kuslar), print(type(kuslar))
print(len(kuslar)) 
  
kuslar = {"karga","serçe","kuzgun","kartal"}

for x in kuslar:
  print(x)

kuslar = {"karga","serçe","kuzgun","kartal"} 
print("serçe" in kuslar) #This is boolean

kuslar.add("atmaca")
print(kuslar)


        #Dictionary 

biscuit = {
    'brand':'Ülker',
    'price': 5.50,
    'expiration date': 2021,
    'types' : ['chocolate','strawberrry','caramel']
}
print(biscuit)
print(biscuit['brand'])
print(len(biscuit))
print(type(biscuit))

yu=biscuit['price']
print(yu)


g= biscuit.items()
print(g)

biscuit.update({'price': 6.50})
print(biscuit)

biscuit.update({'ingredients' : 'No gluten'})
print(biscuit)



