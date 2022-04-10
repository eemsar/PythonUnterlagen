#Um einen Error vorzubeugen können 'try'-, 'except'-, 'else'- & 'finally'-Blöcke genutzt werden. Diese können auch verschachtelt werden.
#Mit dem try-Block wird ein kritischer Bereich auf Fehler getestet.
#Mit dem except-Block können Fehler behandelt werden.
#Der else-Block wird ausgeführt wenn kein Fehler auftritt.
#Der finally-Block wird immer ausgeführt.

try:
    f = open("demofile.txt")
    try:
        f.write("Test")
    except:
        print("Es konnte nicht in die Datei geschrieben werden.")
    finally:
        f.close()
except:
    print("Die Datei konnte nicht geöffnet werden.")   
    
    
#Beim Auftreten bestimmter Bedingungen kann eine Exception mit dem Keyword 'raise' und dem dazugehörigen Namen ausgeführt werden. (siehe iterator.py)