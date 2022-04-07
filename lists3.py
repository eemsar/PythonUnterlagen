a = [1,2,3,4,5,6]
b = [100,200,300,400,500]

#Das Hinzufügen eines neuen Elements ganz hinten an die Liste erfolgt mit der append-Methode
a.append("letztes Element")
print(a)

#Eine Liste kann um eine andere Liste, Set, Tuple oder Dictionary erweitert werden mit der extend-Methode
a.extend(b)
print(a)

#Hinzufügen eines neuen Elements an die ausgewählte Stelle (die restlichen Elemente rutschen nach rechts).
a.insert(2,"Neues Element")
print(a)

#Listen werden kopiert in dem die Referenz der einen Liste mit der anderen geteilt wird (Nachteil: wenn die eine Liste verändert wird
#ändern sich die Werte der anderen Liste ebenfalls.
a = b.copy()
print(a)