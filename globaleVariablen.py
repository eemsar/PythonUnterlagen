#Globale Variablen

x = "Die Variable x ist global gültig"
print(x)

def globalX():
    print("\n" + x)

def lokalX():
    x = "Die Variable x ist lokal in der lokalX-Methode vorhanden"
    print("\n" + x)
    
def lokalY():
    global y 
    y = "Die Variable 'y' ist global"
    print("\n" + y)
    
globalX()
lokalX()
lokalY()    
print("\n" + y + " auch außerhalb der 'lokalY-Methode', nachdem die lokalY-Methode ausgeführt worden ist.")
  