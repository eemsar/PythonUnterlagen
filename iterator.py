#Ein Iterator ist ein Objekt, dessens Elemente duruchlaufen werden kann.
#Um so ein Objekt erstellen zu können, muss die Funktion eine __iter__()- & eine __next__()-Funktion besitzen.
#Die __iter__-Funktion gibt das aktuelle Objekt zurück (somit den aktuellen Zustand/Wert des Objekts).
#Die __next__-Funktion gibt das nächste Element im Objekt zurück.

class Iter:
    def __init__(self, anfang, ende):
        self.anfang = anfang
        self.ende = ende
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.anfang >= self.ende:
            raise StopIteration
        aktuellerWert = self.anfang
        self.anfang += 1
        return aktuellerWert

zahlenBereich = Iter(2,8)

for x in zahlenBereich:
    print(x)            