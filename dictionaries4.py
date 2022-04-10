#Dictionaries können mit der copy-Methode kopiert werden.
a = {
    "eins" : 1,
    "zwei" : 2,
    "drei" : 3,
    "vier" : 4
}
b = a.copy()
print(b)

#Dictionaries können als Value in andere Dictionaries eingebettet werden
e = {
    "zahlen" : {
        "eins" : 1,
        "zwei" : 2,
        "drei" : 3,
        "vier" : 4
    }
}
print(e)