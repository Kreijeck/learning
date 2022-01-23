import argparse

# Castet Argumente zu passendem Typ!
def check_for_boolean_value(val):
    if isinstance(val, bool):
        return val
    if val == "True":
        return True
    else:
        return False

def main():
    # name: --age : für commandline
    # dest: my_age: speichert er als my age ab
    # parser.add_argument("--age", help="Enter your age (int)",
    #                       type=int, required=True, dest="myAge")
    # age = args.myAge

    parser = argparse.ArgumentParser()
    parser.add_argument("--age", help="Enter your age (int)", type=int, required=True)
    parser.add_argument("--name", help="Enter your name (str)", type=str, required=True)
    # in type kann auch funktion verwendet werden und nimmt dort den Type ein
    # default=True und argument wird nicht angegeben, ist Wert automatisch True (bei type bool)
    parser.add_argument("--admin", help="Are your an admin? (bool)",
                        type=check_for_boolean_value, required=False, default=False)
    args = parser.parse_args()
    age = args.age
    name = args.name
    is_admin = args.admin
    print(age, type(age))
    print(name, type(name))
    print(is_admin, type(is_admin))

if __name__ == "__main__":
    main()
