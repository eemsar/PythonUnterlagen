#Dictionaries bestehen aus Key-/Valuepaaren. Dictionaries sind geordnet, veränderbar und erlauben keine Duplikate.

#Zugriff mit Hilfe der Keys
a = {
    "eins" : 1,
    "zwei" : 2,
    "drei" : 3
}
print(a)
print(a["drei"])

#Anzeige aller Keys der Dictionary mit keys-Methode
x = a.keys()
print(x)

#Zuweisung neues Key-/Valuepaar. Es kann bereits vorhanden Keys neue Values zugewiesen werden.
a["vier"] = 4
print(a)

#Anzeige aller Values mit values-Methode
y = a.values()
print(y)

#Abbildung aller Key-/Valuepaare als Tuples in einer Liste
z = a.items()
print(z)

#Zuweisung neues Key-/Valuepaar oder Zuweisung an einem bereits vorhanden Key mit update-Methode
b = {"Steve": "Jobs", "Elon" : "Musk"}
a.update(b)
print(a)