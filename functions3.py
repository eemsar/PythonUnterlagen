#Funktionen können mit dem Keyword 'return' einen Wert zurückliefern. 
#Mit dem Keyword 'pass' als einzige Anweisung kann eine Funktion erstellt werden, die keinen Error ausgibt, wenn Sdie Funktion keine weiteren Anweisungen besitzt.
#Das Konzept der Rekursion ist in Python ebenfalls verankert.

def fakultaet(zahl):
    if zahl > 1:
        return zahl * fakultaet(zahl-1)
    else:
        return 1

zahlFürFakultät = int(input("Geben Sie bitte eine positive Zahl ein, von der die Fakultät bestimmt werden soll: "))


while True:
    if zahlFürFakultät < 0:
        zahlFürFakultät = int(input("Geben Sie bitte eine positive Zahl ein, von der die Fakultät bestimmt werden soll: "))
    else:
        break
    
print(fakultaet(zahlFürFakultät))

