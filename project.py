import json
import os

CONTACTS_FILE = "contacts.json"

def main():
    contacts = load_contacts()
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            name = input("Enter name: ").strip()
            phone = input("Enter phone: ").strip()
            email = input("Enter email: ").strip()
            if add_contact(contacts, name, phone, email):
                print(f"Contact {name} added successfully.")
            else:
                print(f"Contact {name} already exists.")

        elif choice == "2":
            print("\nContacts:")
            print(view_contacts(contacts))

        elif choice == "3":
            name = input("Enter name to search: ").strip()
            contact = search_contact(contacts, name)
            if contact:
                print(f"Found Contact - Name: {name}, Phone: {contact['phone']}, Email: {contact['email']}")
            else:
                print(f"Contact {name} not found.")

        elif choice == "4":
            name = input("Enter name to delete: ").strip()
            if delete_contact(contacts, name):
                print(f"Contact {name} deleted successfully.")
            else:
                print(f"Contact {name} not found.")

        elif choice == "5":
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-5.")

# -------------------- Functions --------------------

def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return {}
    with open(CONTACTS_FILE, "r") as f:
        return json.load(f)

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts, name, phone, email):
    if name in contacts:
        return False  # Contact already exists
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    return True

def view_contacts(contacts):
    if not contacts:
        return "No contacts found."
    result = []
    for name, info in contacts.items():
        result.append(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    return "\n".join(result)

def search_contact(contacts, name):
    return contacts.get(name, None)

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        return True
    return False


if __name__ == "__main__":
    main()
