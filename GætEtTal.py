import random

RigtigTal = random.randrange(1, 3)
print("hvad gætter du på")
gæt = input()
print("dit gæt " + gæt )
if( gæt == RigtigTal):
   print("rigtig!")
if( gæt != RigtigTal):
   print("Forkert!")
   print("det rigtig svar var " + str(RigtigTal))