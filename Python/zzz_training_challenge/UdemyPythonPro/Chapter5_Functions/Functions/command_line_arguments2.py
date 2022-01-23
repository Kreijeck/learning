import argparse

def main():
    # erstellt parser
    parser = argparse.ArgumentParser()
    # Argumente hinzufügen:
    # Name: default mit '--' <- Konvention
    # help: Optional als Hilfe
    # type: Optional: Typ
    # required: Wird das argument pflichtend benötigt
    #
    parser.add_argument("--age", help="Enter your age (int)", type=int, required=True)
    parser.add_argument("--name", help="Enter your name (str)", type=str, required=True)
    parser.add_argument("--admin", help="Are your an admin? (bool)", type=bool, required=False)

    # Einlesen und Zugreifen der Parameter
    args = parser.parse_args()
    age = args.age
    name = args.name
    is_admin = args.admin
    print(age, type(age))
    print(name, type(name))
    # Achtung Argumente werden als Strings abgespeichert!! auch wenn Type = bool
    #  Das heißt auch wenn im Argument  "False" angegeben
    # wird ist dies kein leerer String und damit "True"
    print(is_admin, type(is_admin))


if __name__ == "__main__":
    main()
