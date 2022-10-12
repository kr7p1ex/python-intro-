from distutils.log import debug

animale1 = "hund"
animale2 = "blå tunget skin"
animale3 = "cat"
All_Animales =[animale1,animale2,animale3]
All_AnimalesAge = [14,5,20]
havefoundpet = ""
prisForpet = 10
yourMoney = 50

print("look for pet")
print(bool(havefoundpet))

#denne function tjekker alle dyrene i Animale arrayen og printer ud når den har fundet hund

def SeachforPet(Animales,Age):
  print("lokking for pet")
  for animal in Animales:
    i = Animales.index(animal)
    if animal == Animales[0]:
        print("found pet"+ " " + animal + " " str(Age[i])  )

        havefoundpet ="yes"

        print(bool(havefoundpet))

        print("the pet cost %d"  % prisForpet)
        print("buy pet")
        print ("leftover money ",yourMoney-prisForpet)
  
SeachforPet(All_Animales,All_AnimalesAge)
