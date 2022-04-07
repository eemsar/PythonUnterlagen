a = [1,2,3,4,5,6]

#Einen Wert aus der Liste verändern
a[0] = 11
print("Der neue 0.te Wert heißt: " + str(a[0]))
print("Die neue Liste lautet: " + str(a))

#Die neuen Elemente nehmen die Plätze der alten ein und schieben die anderen alten Elemente nach hinten
a[1:3] = 100,200,300
print("Die Listet lautet: " + str(a) + " nachdem die neuen Elemente eingerückt worden sind.")

