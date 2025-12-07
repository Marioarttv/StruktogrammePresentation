# Einkaufs-Manager
# Ein Programm zum Verwalten einer Einkaufsliste

# 1. Leere Liste erstellen
einkaufsliste = []

# 2. Variable für die Schleife
running = True

# 3. Endlos-Schleife (solange running wahr ist)
while running:
    
    # 4. Menü anzeigen
    print("\n--- MENÜ ---")
    print("1: Hinzufügen")
    print("2: Anzeigen")
    print("3: Ende")
    
    # 5. Auswahl abfragen
    wahl = input("Deine Wahl: ")
    
    # 6. Verzweigung: Was soll passieren?
    if wahl == "1":
        produkt = input("Was möchtest du hinzufügen? ")
        einkaufsliste.append(produkt)
        print(produkt + " wurde hinzugefügt.")
        
    elif wahl == "2":
        print("Deine Einkaufsliste:")
        # Schleife durch die Liste
        for item in einkaufsliste:
            print("- " + item)
            
    elif wahl == "3":
        print("Tschüss!")
        running = False
        
    else:
        print("Ungültige Eingabe!")
