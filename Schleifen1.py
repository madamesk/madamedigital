x = input("Bitte geben Sie eine Ganzzahl ein: ")

x = int(x)

print("x hat aktuell folgenden Wert:", x)
print()
if x < 5:
    print("x ist kleiner als 5")

elif x == 5:
    print("x entspricht haargenau 5")

else:
    print(x, " ist größer als 5")