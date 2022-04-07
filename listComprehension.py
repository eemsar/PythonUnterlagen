#List Comprehension dienen dazu, mit einem kürzeren Syntax eine Schleife durchzulaufen.
#Der Aufbau sieht wie folgt aus: [expression for element in iterable if condition]


a = [1,2,3,4,5,6]
[print(x) for x in a]


#-------------------------------------------------------------------------------------
"""
Statt:
c = ["apfel","banane","kirsche","kiwi","mango"]
d = []

for x in c:
    if "a" in x:
        d.append(x)
print(d)
"""

c = ["apfel","banane","kirsche","kiwi","mango"]
d = [x for x in c if "a" in x]
print(d)
#-------------------------------------------------------------------------------------
#Wenn eine else genutzt werden soll kommt das if und else vor die for-Schleife
früchte = ["apple", "banana", "cherry", "kiwi", "mango", "orange"]
z = [x if x != "banana" else "orange" for x in früchte]
print(z)