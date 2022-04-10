#for-loops nutzen ebenfalls die Keywords 'break und 'continue', um eine Sequenz zu überspringen oder das Durchlaufen komplett zu beenden.
#for-loops können auch in einander verschachtelt werden.

countCombination = 0
for x in range (0, 55 , 5):
    for y in range(10, 32, 2):
        print(x,y)
        countCombination += 1

print("Es sind " + str(countCombination) +" Kombinationen vorhanden.")
#Das Keyword 'pass' ist auch in einer for-loop möglich.