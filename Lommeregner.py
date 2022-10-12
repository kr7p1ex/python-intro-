print('hvad vil du beregne:')
FørsteTal= input()
print("hvad vil du gøre med det her tal?, " + FørsteTal)
Condistion = input()
print("hvad er det andet tal du vil bruge?")
AndenTal= input()
if (Condistion == "+"):
    Resutalt = float(FørsteTal) + float(AndenTal)

if (Condistion == "-"):
    Resutalt = float(FørsteTal) - float(AndenTal)

if (Condistion == "*"):
    Resutalt = float(FørsteTal) * float(AndenTal)

if (Condistion == "/"):
    Resutalt = float(FørsteTal) / float(AndenTal)

if (Condistion == "%"):
    Resutalt = float(FørsteTal) % float(AndenTal)

if (Condistion == "**"):
    Resutalt = float(FørsteTal) ** float(AndenTal)

if (Condistion == "//"):
    Resutalt = float(FørsteTal) // float(AndenTal)


print(Resutalt) 
