#Zugriffe auf bestimmte Teilbereiche
beispielString = "Die Zeichenkette wird einmal durchlaufen"

#Ausgabe der Länge des Strings
print(len(beispielString))

#Zugriff auf das 0.te Element
print(beispielString[0])

#Überprüfung, ob ein Wort im String vorkommt
print("Zeichenkette" in beispielString)

#Ausgabe von "Die Zeichenkette" -> Festlegung einer bestimmten Zeichenreichweite. Die zweite Zahl ist nicht inklusive.
print(beispielString[0:16])

#Es werden alle Zeichen ausgegeben und die restlichen Stellen sind leer
print(beispielString[0:100])

#Abkürzung für Zugriff ab dem 0.ten Zeichen bis zum letzten Zeichen
print(beispielString[:100])

#Abkürzung für Zugriff ab dem 4.ten Zeichen bis zum letzten Zeichen
print(beispielString[4:])

#Der String wird von hinten ausgewertet
print(beispielString[-11:-6])

