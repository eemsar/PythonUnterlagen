#Sets sind nicht geordnet, die Werte nicht veränderbar und Duplikate nicht erlaubt.

a = {1,2,3,4,5}
print(a)

#Zugriff über for Schleife
for x in a:
    print(x)
    
print()    

#Hinzufügen ein neues Element mit der add-Methode
a.add("letzter Beitrag")
print(a)

print()

#Elemente können mit der remove- oder der discard-Methode gelöscht werden (die remove-Methode gibt einen Fehler aus wenn das zu löschen Element nicht vorhanden
#ist, die discard-Methode gibt keinen Fehler aus).
a.remove("letzter Beitrag")
a.discard("byebye")
print(a)

print()

#Sets können um eine andere Collection(List/Tuple/Dictionary) mit der update Methode erweitert werden. 
#Die union-Methode hat die selbe Funktion, nur beschränkt sich die Methode auf Sets. 
b = [100,200,300]
c = {"A","B","C"}
a.update(b)
d = a

e = a.union(c)
print(d)
print(e)
