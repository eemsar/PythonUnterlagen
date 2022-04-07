#Listen sind geordnet, die Werte sind veränderbar und Duplikate erlaubt. Mit geordnet ist gemeint, dass die Struktur der Liste fest definiert ist und mit einem
#Index immer auf das selbe Element zugegriffen wird. 

a = [1, 2, 3, [100,200,300], True, "letztes Element"]
print(a)

#Zugriffsmethoden wie bei strings2.py
print(a[1:4])

#Überprüfen, ob ein Element in der Liste vorhanden ist (input-Methode liefert immer einen String, daher können nur Strings überprüft werden)
if input("Geben Sie ein welches Zeichen überprüft werden soll: ") in a:
    print("Das Element ist vorhanden")
else:
    print("Das Element existiert nicht in der Liste")
    
    
