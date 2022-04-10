#Jede '.py'-Datei ist ein Modul, welches alleinstehend oder als importiertes Modul ausgeführt werden kann. 
#Beim ausführen jedes Moduls werden gewisse Werte initialisiert. Hierzu zählt die Variable '__name__' die den Wert main erhält, wenn das eigene
#Modul als Anfangspunkt ausgeführt wird. Wenn ein Modul von einem externen Modul ausgeführt wird, erhält man statt __main__ für die Variable __name__ ,
#den Namen des Moduls (ohne .py - Endung). Dies kann genutzt werden um gewisse Codebereiche nur auszuführen, wenn ein Modul als Startpunkt dient.

if __name__ == "__main__":
    print("Das Modul 'entrypoint.py' entspricht dem Entrypoint und die Variable __name__ lautet: " + __name__)
else:
    print("Der Entrypoint entspricht 'entrypoint2.py' und die Variable __name__ lautet: " + __name__)