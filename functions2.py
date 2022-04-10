#Wenn die Anzahl der zu aufnehmenden Parameter zuvor unbekannt ist, können 'arbitrary arguments' genutzt werden. Dieser nimmt einen Tupel an Werten auf.
#Abkürzungen in den docs als *args

def lebensmittelAnzeige(*lebensmittel):
    print("Sie haben sich für: " + lebensmittel[1] + " entschieden")
    
lebensmittelAnzeige("Apfel", "Brot", "Fisch")



#Um in der Funktion Parameter mit den Namen nutzen zu können, können 'keyword arguments' genutzt werden. 
#Sie haben den Vorteil, dass die Reihenfolge der Parameter und der Arguement nicht übereinstimmen muss, da durch die Namen eine Übereinstimmung erfolgt.
#Abkürzun in den docs als kwargs

def fastfoodGerichte(fastfood_2, fastfood_3, fastfood_1):
    print("Die Fastfood-Gerichte lauten: " + fastfood_3, fastfood_1, fastfood_2)
    
fastfoodGerichte(fastfood_1 = "Döner", fastfood_2 = "Pizza", fastfood_3 = "Nudeln")


#Als letztes gibt es das Konzept der 'arbitary keyword arguments'. Hier werden die Konzepte der 'abitary & keyword arguments' vereint.
#Die Argumente werden Variablen zugewiesen und beim Funktionsaufruf übergeben. Die Funktion erhält eine Dictionary an Werten und kann sie nutzen.
#Abkürzungen in den docs als **kwargs

def tierSorten(**tiere):
    print("Die Tiere, die sich in der Liste befinden heißen: " + tiere["säugetier1"], tiere["säugetier2"] + " und " + tiere["fisch"])
    
tierSorten(säugetier1 = "Hund" , säugetier2 = "Katze", fisch = "Hai")


#Funktionen können Defaultwerte besitzen. Diese initialisieren ein Parameter mit einem Wert, beim Fehlen des Arguments.

def defaultWert(produkt = "Milch"):
    print("Das Produkt das Sie kaufen heißt: " + produkt)
    
defaultWert("Käse")
defaultWert("Tomate")
defaultWert("Brot")
defaultWert()