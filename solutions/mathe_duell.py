# Mathe-Duell
# Ein kleines Rechenspiel mit Zufallszahlen

import random

# 1. Leere Liste für Ergebnisse (Richtig/Falsch)
ergebnisse = []

print("Willkommen zum Mathe-Duell! Löse 5 Aufgaben.")

# 2. Schleife: Genau 5 Runden
for i in range(5):
    
    # 3. Zufallszahlen generieren (zwischen 1 und 20)
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    
    # 4. Aufgabe stellen
    print("Aufgabe " + str(i+1) + ": Was ist " + str(a) + " + " + str(b) + "?")
    
    # 5. Eingabe (muss in Zahl umgewandelt werden!)
    antwort = int(input("Ergebnis: "))
    
    # 6. Verzweigung: Prüfen
    if antwort == a + b:
        print("Richtig!")
        ergebnisse.append("Richtig")
    else:
        print("Falsch! Das Ergebnis war " + str(a + b))
        ergebnisse.append("Falsch")

# 7. Auswertung am Ende
print("\nDeine Ergebnisse:")
print(ergebnisse)
