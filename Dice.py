import random

def Rulltegning6():
    RulletTal = random.randrange(1, 6)
    print(str(RulletTal))
    print("vil du slå igen?")
    Andensvar=input()
    if(Andensvar == "ja"):
      HvilkeTergning()
    print("hvorfor ikke >:(")

def Rulltegning20():
    RulletTal = random.randrange(1, 20)
    print(str(RulletTal))
    print("vil du slå igen?")
    Andensvar=input()
    if(Andensvar == "ja"):
      HvilkeTergning()
    print("hvorfor ikke >:(")

def Rulltegning4():
    RulletTal2 = random.randrange(1, 4)
    print(str(RulletTal2))
    print("vil du slå igen?")
    Andensvar=input()
    if(Andensvar == "ja"):
      HvilkeTergning()
    print("hvorfor ikke >:(")





def HvilkeTergning():
 print("hvilken tegning? 4, 6 eller 20")
 valgteTergnig = input()
 if(valgteTergnig== "6"):
    Rulltegning6()
 if(valgteTergnig== "20"):
    Rulltegning20()
 if(valgteTergnig== "4"):
    Rulltegning4()
    

   

print("Vil du slå tegning")
FørstSvar = input()
if(FørstSvar == "ja"):
  HvilkeTergning()

print("hvorfor ikke >:(")




