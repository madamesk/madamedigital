import random # die Bibliothek wird importiert

random.seed() # Die Zufallszahlen werden initialisiert

zahl = random.randint(1,10) # Hier wird eine Zufallszahl generiert, die zwischen 1 und 10 liegt.
print(zahl)
eingabe = int(input("Bitte geben Sie eine Zahl zwischen 1 und 10 an: ")) # String in Integer umwandeln


if zahl == eingabe: 
    print("Gratulation! Richtig geraten!")
else:
    print("Leider falsch!")