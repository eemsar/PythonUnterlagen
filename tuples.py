#Tuples sind geordnet, nicht veränderbar (indirekt möglich, indem der Tuple erst in eine Liste umgewandelt wird, die Änderung vorgenommen und dann die Liste
#zurück in ein Tuple umgewandelt wird) & Duplikate sind erlaubt.

#Zugriff durch Index
a = (1,2,3,4,5,6,7)
print(a)
print(a[2])

#Weitere Zugriffe wie bei Strings möglich
print(a[-5:-2])

#Wenn Tuple mit einem Element erstellt wird muss ein Komma genutzt werden
b = ("Ein Wert",)
print(b)
print(type(b))
print() 

#Die Werte eines Tuples können durch das 'Unpacking neuen Werten zugewiesen. Mit dem Asterisk können einer Liste mehrere Werte zugewiesen werden.
c = (1,2,3,4,5,6,7)
(ersteZahl,*listeMitZahlen,letzteZahl) = c
print(ersteZahl)
print(listeMitZahlen)
print(letzteZahl)

