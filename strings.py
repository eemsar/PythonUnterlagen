#Stringzuweisungen
string1 = "String 1"
string2 = '\nString 2'

mehrZeilenString1 = """\nmehrZeilenString1 beginnt hier
Zeile 1
Zeile 2
Zeile 3
mehrZeilenString1 endet hier"""

mehrZeilenString2 = '''\nmehrZeilenString2 beginnt hier
Zeile 1
Zeile 2
Zeile 3
mehrZeilenString2 endet hier'''

intValue = 5

print(string1)
print(string2)
print(mehrZeilenString1)
print(mehrZeilenString2)
print("\nDie int-Variable 'intValue' wird mit der str()-Methode in ein String umgewandelt und ergibt dann: " + str(intValue))