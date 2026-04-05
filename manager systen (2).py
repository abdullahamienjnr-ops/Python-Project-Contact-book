# contact book

contacts = {}

def add_contact():
    name = input("name: ").strip()
    phone = input("phone: ").strip()

    if not name or not phone:
        print("name and phone cannot be empty")
        return

    contacts[name] = phone
    print(f"saved: {name} == {phone}")

def search_contact():
    name = input("search name: ").strip()
    if not name:
        print("name cannot be empty")
        return

    phone = contacts.get(name)
    if phone:
        print(f"{name} == {phone}")
    else:
        print(f"{name} not found")

def update_contact():
    name = input("name to update: ").strip()
    if name not in contacts:
        print("contact not found")
        return

    new_phone = input("new phone number: ").strip()
    if not new_phone:
        print("phone cannot be empty")
        return

    contacts[name] = new_phone
    print(f"updated: {name} == {new_phone}")

def view_all():
    if not contacts:
        print("(no contacts yet)")
        return
    print("--- contacts ---")
    for name, phone in contacts.items():
        print(f"{name} == {phone}")

def menu():
    print("contact book")
    print("1) add contact")
    print("2) search contact")
    print("3) update contact")
    print("4) view all")
    print("5) exit")

def main():
    while True:
        menu()
        choice = input("choose an option: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            view_all()
        elif choice == "5":
            print("goodbye!")
            break
        else:
            print("please choose 1, 2, 3, 4, or 5")

if __name__ == "__main__":
    main()
