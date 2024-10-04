task = input ("Bitte gib eine Aufgabe ein, die zur Aufgabenliste hinzugefügt werden soll: ")
due_date = input("Bitte gib das Fälligkeitsdatum für die Aufgabe an: ")
def tasklist():
    print(f"Die Aufgabe {task} wurde zur Liste hinzugefügt.")

if not tasklist:
    print("Deine Aufgabenliste ist leer.")
    for task in tasklist:
        print(f"Aufgabe: {task}, Fälligkeitsdatum :{due_date} ")

while True:
    print("\n----- Aufgabenliste -----")
    print("1. Aufgabe hinzufügen")
    print("2. Aufgabenliste anzeigen")
    print("3. Programm beenden")
    choice = input("Bitte wähle 1,2 oder 3: ")

    if choice == '1':
        task()
    elif choice == '2':
        tasklist()
    elif choice == '3':
        print("Programm wird beendet. Auf Wiedersehen!")
        break
    else:
        print("Ungültige Auswahl. Bitte wähle 1,2 oder 3.")

def remove_task():
    task = input("Bitte gib die Aufgabe ein die entfernt werden soll: ")
    for t in tasklist:
        if t["Aufgabe"] == task:
            tasklist.remove(t)
            print(f"Die Aufgabe {task} wurde entfernt.")

        if __name__ == "__main__":
            main()