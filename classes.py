#Python ist eine objektorientierte Programmiersprache. D.h. jede Klasse ist ein Objektkonstruktor/Blueprint für seine Objekte. 
#Die '__init__()'-Funktion ist dabei der Standardkonstruktor der Klasse, um so das Objekt mit Werten zu initialisieren.
#Mit dem Keyword 'self' wird das aktuelle Objekt angesprochen. Statt 'self' kann auch ein anderer Name für diesen Parameter gewählt werden,
#jedoch entspricht 'self' dem Standard.

class Person:
    def __init__(self,vorname,nachname, alter):
        self.vorname = vorname
        self.nachname = nachname
        self.alter = alter
        print("Sie heißen: " + self.vorname + " " + self.nachname)

    def alterPrint(self):
        print("Sie sind: " + self.alter + " Jahre alt")
        
#Die Objekterstellung, erfolt über den Klassennamen.
person_1 = Person(input("Geben Sie Ihren Vornamen ein: "), input("Geben Sie Ihren Nachnamen ein: "), input("Geben Sie Ihr alter an: "))
person_1.alterPrint()

#Die Attribute eines Objekts können mit dem Keyword 'del' gelöscht werden. Mit dem Keyword 'del' kann auch das gesamte Objekt gelöscht werden.
#Eine leere Klasse die fehlerfrei laufen soll, muss eine 'pass'-Anweisung besitzen.