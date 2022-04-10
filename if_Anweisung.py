#Beispiel_1 für if,else if und else
a = 10
b = 10
if a > b:
    print("a ist größer als b")
elif a < b:
    print("a ist kleiner als b")
else:
    print("a und b sind gleich groß")
    
#Kurzform für das gleiche Beispiel (Beispiel_1)
#Aufbau:(expression_1 if condition1 else expression_2 if condition2 else expression_3)
print("a ist kleiner als b " if a < b else "a ist größer b" if a > b else "a und b sind gleich groß")

#Beispiel_2 Überprüfung mehrer conditions können über die Keywords 'and' & 'or' erreicht werden
a = int(input("Geben sie a ein: "))
b = 22
if a > b and a > 50 and a > 90:
    print("a ist größer als b (22), größer als 50 und größer als 90")
elif a > b and a > 50 and a < 90:
    print("a ist größer als b (22), größer als 50 und kleiner als 90")
else:
    print("a ist kleiner als 22 oder kleiner als 50")

#Wenn nach einem if-Anweisung kein Befehl im Block folgt, erhält man einen Fehler. Eine Vermeidung ist durch das Keyword 'pass' möglich.