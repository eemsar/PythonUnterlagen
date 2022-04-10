#String Formatting kann mit Hilfe von geschweiften Klammern erfolgen. Die geschweiften Klammern dienen als Platzhalter.

#Beispiel 1
try:
    name = input("Wie heißen Sie? ")
    alter = input("Wie alt sind Sie? ")
    txt = "Sie heißen: {} und sind {} Jahre alt"
    print(txt.format(name,alter))
except:
    print("Es gab ein Problem bei Ihren Eingaben")
    
#Beispiel 2
try:
    partner = input("Wie heißt Ihr Partner? ")
    partner_alter = input("Wie alt ist Ihr Partner? ")
    txt = "Er/Sie heißt {0}. {0} ist {1} Jahre alt."
    print(txt.format(partner,partner_alter))
except:
    print("Es gab ein Problem bei Ihren Eingaben")