#Lambdafunktionen, auch anonyme functions genannt, sind Einweg-functions in Python. 

x = lambda a,b: a + b 
zahl_1 = int(input("Geben Sie die erste Zahl für die Addition ein: "))
zahl_2 = int(input("Geben Sie die zweite Zahl für die Addition ein: "))
print("Das Ergebnis der Addition lautet: " + str(x(zahl_1,zahl_2)))