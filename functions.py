vorname = input("Geben Sie ihren Vornamen ein: ")
nachname = input("Geben Sie ihren Nachnamen ein: ")

#Funktionen werden in Blöcke aufgeteilt. Jede Funktion hat eine Parameterliste, die mehrere Parameter aufnehmen kann. 
def ausgabeName(vorname, nachname):
    print("Sie heißen: " + vorname + " " + nachname)

#Der Funktionsaufruf geschieht mit dem Namen. Zudem können Argumente übergeben werden, die von der Funktion als Parameter genutzt werden.
ausgabeName(vorname,nachname)




