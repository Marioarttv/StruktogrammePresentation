# Taxi-Rechner
# Berechnet den Fahrpreis basierend auf Distanz und Währung

# 1. Preise festlegen (Basiswerte in Euro)
grundpreis = 3.50
preis_pro_km = 2.00

# 2. Begrüßung und Währungsauswahl
print("Willkommen beim Taxi-Rechner!")
print("Wähle die Währung:")
print("1 = Euro (€)")
print("2 = Dollar ($)")

# 3. Eingabe der Währung
waehrung = input("Deine Wahl: ")

# 4. Verzweigung: Welche Währung?
if waehrung == "1":
    symbol = "€"
    # Preise bleiben in Euro
else:
    symbol = "$"
    # Umrechnung in Dollar (Kurs: 1 EUR = 1.10 USD)
    grundpreis = grundpreis * 1.10
    preis_pro_km = preis_pro_km * 1.10

# 5. Distanz abfragen
print("Wie viele Kilometer möchtest du fahren?")
distanz = float(input("Distanz in km: "))

# 6. Gesamtpreis berechnen
gesamtpreis = grundpreis + (distanz * preis_pro_km)

# 7. Ergebnis ausgeben
print("---")
print("Grundpreis: " + str(round(grundpreis, 2)) + " " + symbol)
print("Strecke: " + str(distanz) + " km")
print("Kilometerpreis: " + str(round(preis_pro_km, 2)) + " " + symbol + "/km")
print("---")
print("Gesamtpreis: " + str(round(gesamtpreis, 2)) + " " + symbol)
