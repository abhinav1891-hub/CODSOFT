# Contact Book Application
# CodSoft Internship Task

contacts = []

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("Contact added successfully ✅")


def view_contacts():
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")


def search_contact():
    search = input("\nEnter name or phone to search: ").lower()
    found = False

    for contact in contacts:
        if search in contact["name"].lower() or search in contact["phone"]:
            print("\nContact Found:")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])
            found = True

    if not found:
        print("Contact not found ❌")


def update_contact():
    name = input("\nEnter name of contact to update: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            print("Enter new details:")
            contact["phone"] = input("New Phone: ")
            contact["email"] = input("New Email: ")
            contact["address"] = input("New Address: ")
            print("Contact updated successfully ✅")
            return

    print("Contact not found ❌")


def delete_contact():
    name = input("\nEnter name of contact to delete: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            print("Contact deleted successfully 🗑️")
            return

    print("Contact not found ❌")


# Main menu
while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()

    elif choice == '2':
        view_contacts()

    elif choice == '3':
        search_contact()

    elif choice == '4':
        update_contact()

    elif choice == '5':
        delete_contact()

    elif choice == '6':
        print("Exiting... 👋")
        break

    else:
        print("Invalid choice! Try again.")