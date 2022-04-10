#Wie z.B. in Java gibt es auch in Python die Keywords 'break' und 'continue', um eine Schleife frühzeitig zu beenden oder einen Durchgang zu überspringen.
#Die else-Anweisung tritt nur in Kraft, wenn die Schleife komplett durchlaufen wird und nicht frühzeitig beendet wird.

i = 0
while i < 7:
    print(i)
    if i == 5:
        break
    i += 1
else:
    print("Die Schleife wurde bis zum Ende ausgeführt.")    