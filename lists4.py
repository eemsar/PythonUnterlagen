a = [1,2,3,4,5,6]
print(a)

#Löschen eines bestimmten Elements mit der remove-Methode
a.remove(2)
print(a)

a.insert(1, 2)
print(a)

#Ein bestimmtes Element (mit einem Index) löschen mit der pop-Methode oder dem Keyword 'del'
a.pop(2)
print(a)

a.insert(2, 3)
print(a)

del a[4]
print(a)

a.insert(4, 5)
print(a)

#Liste komplett bereinigen
a.clear()
print(a)

a = [1,2,3,4,5,6]
print(a)

#Die Liste komplett löschen mit dem Keyword 'del'
del a
print(a)