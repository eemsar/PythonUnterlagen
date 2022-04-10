#Das Konzept der Inheritance/Vererbung ist in Python auch vorhanden. Hierzu wird dem 'child class' (der erbenden Klasse)
#der 'parent class' (Basisklasse) als Parameter übergeben. Dadurch können die Funktionen & Variablen der parent class genutzt werden.
#Die __init__-Funktion der parent class kann von der child class genutzt oder auch erweitert werden, wenn weitere Attribute in der child class
#hinzukommen. Mit 'super().' wird auf die __init__-Funktion der parent class zugegriffen. 

class Person:
    def __init__(self, vorname, nachname):
        self.vorname = vorname
        self.nachname = nachname
        
    def printName(self):
        print("Sie heißen: " + self.vorname, self.nachname)
        
class Student(Person):
    def __init__(self, vorname, nachname, alter):
        super().__init__(vorname, nachname)
        self.alter = alter

    def printAlter(self):
        print("Sie sind: " + self.alter + " Jahre alt.")
        
student = Student(input("Geben Sie Ihren Vornamen ein: "), input("Geben Sie Ihren Nachnamen ein: "), input("Geben Sie Ihr alter an: "))
student.printName()
student.printAlter()