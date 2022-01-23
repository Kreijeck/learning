# Konstanten am Anfang deklarieren und NICHT verändern
# Globale Variablen
POWER_OF = 2


# lokale Variable a (referenz), b (lokal)
def my_function(a):
    b = a**POWER_OF
    print(a, b)


# in diesem Punkt kann nicht auf my_int_value zugegriffen werden

def main():
    my_int_value = 3
    my_function(my_int_value)
    # dir Funktion: welche methoden besitzt eine Variable/Methode/Klasse
    print(dir(my_int_value))
    print()
    # Show Global and locals in current scope
    print("Globals:")
    print(globals())
    print("Locals:")
    print(locals())


# Main Datei wenn diese Datei ausgeführt wird.
# Am besten davor nur Methoden verwenden um nicht zusätzlichen Code auszuführen
if __name__ == "__main__":
    main()
