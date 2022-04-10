#Beispiele zum Durchlaufen der Dictionary 

#Beispiel_1
a = {
    "eins" : 1,
    "zwei" : 2,
    "drei" : 3,
    "vier" : 4
}

#Durchlaufen und Anzeige aller Keys
for x in a:
    print(x)

print() 

#Anzeige aller Values
for x in a:
    print(a[x])



#Anzeige aller Key-/Valuepaare
for x,y in a.items():
    print(x,y)