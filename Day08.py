def is_valid_email(email):
    return "@" in email and "." in email

def display_contacts(contacts):
    if not contacts:
        print("No contacts to display.")
    else:
        for i, (name, info) in enumerate(contacts.items(), 1):
            print(f"{i}. {name} | Phone: {info['phone']} | Email: {info['email']}")

def contact_book():
    contacts = {
        "Ali": {"phone": "123", "email": "ali@email.com"},
        "Sara": {"phone": "999", "email": "sara@email.com"}
    }

    while True:
        print("\n📒 Contact Book Menu:")
        print("1. Add New Contact")
        print("2. Update Contact")
        print("3. Retrieve Contact")
        print("4. View All Contacts")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == "1":
            name = input("Enter name: ").title()
            if name in contacts:
                print("Contact already exists.")
                continue
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            if not is_valid_email(email):
                print("Invalid email format.")
                continue
            contacts[name] = {"phone": phone, "email": email}
            print("Contact added successfully.")

        elif choice == "2":
            name = input("Enter name to update: ").title()
            if name not in contacts:
                print("Contact not found.")
                continue
            phone = input("Enter new phone (leave blank to keep unchanged): ")
            email = input("Enter new email (leave blank to keep unchanged): ")

            if phone:
                contacts[name]["phone"] = phone
            if email:
                if not is_valid_email(email):
                    print("Invalid email format.")
                    continue
                contacts[name]["email"] = email
            print("Contact updated.")

        elif choice == "3":
            name = input("Enter name to retrieve: ").title()
            if name in contacts:
                info = contacts[name]
                print(f"{name} → Phone: {info['phone']} | Email: {info['email']}")
            else:
                print("Contact not found.")

        elif choice == "4":
            display_contacts(contacts)

        elif choice == "5":
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please select between 1–5.")

contact_book()
