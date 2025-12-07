# Vokabel-Trainer
# Ein einfaches Programm zum Abfragen von Vokabeln

# 1. Listen für Wörter und Lösungen erstellen
woerter = ["Dog", "Cat", "Mouse"]
loesungen = ["Hund", "Katze", "Maus"]

# 2. Variable für Punkte
punkte = 0

# 3. Schleife über alle Wörter
# Wir nutzen 'range' und 'len', um den Index i zu bekommen (0, 1, 2)
for i in range(len(woerter)):
    
    # 4. Ausgabe der Frage
    print("Was heißt " + woerter[i] + "?")
    
    # 5. Eingabe der Antwort
    antwort = input("Deine Antwort: ")
    
    # 6. Verzweigung: Prüfen ob richtig
    if antwort == loesungen[i]:
        print("Richtig!")
        punkte = punkte + 1
    else:
        print("Falsch! Es wäre " + loesungen[i] + " gewesen.")

# 7. Ausgabe des Endergebnisses
print("Du hast " + str(punkte) + " Punkte erreicht.")
