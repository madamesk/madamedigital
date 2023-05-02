import random # die Bibliothek wird inportiert

for i in 1, 2, 3, 4:  # 4 Runden
    random.seed() 
    zahl = random.randint(1,10)
    
    eingabe = int(input("Bitte geben Sie eine Zahl zwischen 1 und 10 an: "))

    if zahl == eingabe: 
        print("Gratulation! Richtig geraten!")

    else:
        print("Leider falsch!")
        break  # Wenn Falsch geraten wurde, ist man raus!