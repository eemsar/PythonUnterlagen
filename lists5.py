#Durchlaufen der Liste mit der for-Schleife
a = [1,2,3,4,5,6]

for x in a:
    print(x)
    
print()
    
#Durchlaufen der Liste mit der while-Schleife
i = 0 
while i < len(a):
    print(a[i])
    i+=1
    
#Die Sortierung einer Liste mit einheitlicher Datentyp kann über die sort-Methode erfolgen.
b = [22, 3, 14, 66, 20, 1, 32]
b.sort()
print(b)