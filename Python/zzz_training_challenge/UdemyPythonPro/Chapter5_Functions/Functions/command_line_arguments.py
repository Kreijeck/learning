import sys

# per default wird immer der Dateipfad übergeben!
# Arguments werden immer als String interpretiert


def main():
    # Anzahl der Argumente
    print(len(sys.argv))
    # Argumente
    print(sys.argv)
    print("=======================")
    # User-defined command-line arguments
    for arg in sys.argv[1:]:
        print(arg, type(arg))


if __name__ == "__main__":
    main()
