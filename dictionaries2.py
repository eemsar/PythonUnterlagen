#Das Löschen ist möglich wie z.B. bei den Listen mit dem Keyword 'del'. Mit der clear- Methode werden alle Key-/Valuepaare in der Dictionary gelöscht.
#Mit der Methode popitem wird ein zufälliges Element gelöscht. Mit der pop-Methode kann ein ausgewähltes Key-/Valuepaar löschen.

a = {
    "eins" : 1,
    "zwei" : 2,
    "drei" : 3,
    "vier" : 4
}

a.pop("eins")
print(a)
a.popitem()
print(a)