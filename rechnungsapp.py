#Ausgabe Rechnung + Menü
print('********************')
print('')
print('Rechnungerstellungs App')
print('')
print('********************')
print('')
#Eingabe
print('Bitte geben Sie folgend Ihre Daten ein! ')
print('')
firmname = str(input('Firmenname: '))
anschrift = str(input('Firmen Anschrift: '))
f_ust_id = str(input('Ust-ID: '))
while True:
    print('')
    print('Bitte geben Sie folgend die Kunden Daten ein! ')
    print('')
    name = str(input('Name: '))
    vorname = str(input('Vorname: '))
    ust_id = str(input('Ust-ID: '))
    rechnungsnummer = str(input('Rechnungsnummer: '))
    datum = str(input('Datum:'))
    bankdaten = str(input('Bankdaten:'))
    #Preisberechnung pro EInheit oder Projekt
    preis = 0
    anzahl = 1
    antwort_p = ["P", "p"]
    antwort_e = ["E", "e"]
    antwort = input('Soll der Preis pro Einheit oder Projekt berechnet werden? (P/ E) ')
    if antwort in antwort_p:
        preis = float(input('Tragen Sie den Projektpreis ein: '))
        print('Dein Projektpreis beträgt %.2f' % preis, 'Euro/Netto')

    if antwort in antwort_e:
        anzahl = int(input('Tragen Sie die Anzahl ein: '))
        preis = float(input('Tragen Sie Einzelpreis ein: '))
        print('Die Gesamtsumme beträgt %.2f' % (anzahl*preis), 'Euro/Netto')

    #ust anlegen
    ust = 0.19
    antwort_d = ["D", "d"]
    antwort_ewr = ["E", "e"]
    antwort_rest = ["R", "r"]
    antwort = input('In welcher Region befindet sich der Kunde, \n(D) Deutschland \n(E) EWR \n(R) restlichen Welt \n ')
    if antwort in antwort_d:
        print(ust)
    elif antwort in antwort_ewr:
        if len(ust_id) > 0:
            ust = 0.0
        
        print(ust)
    elif antwort in antwort_rest:
        ust = 0.0
        print(ust)

    print("Drucke Rechnung")
    abbruch = input('noch eine Rechnung erstellen? (J/N)')
    if abbruch in ["N","n"]:
        break




    
    


