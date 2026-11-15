"""Contact book with multiple phone numbers and city-wise reports."""

contact_records = {
    "Anita": {"phones": ["9876543210"], "email": "anita@mail.com", "city": "Pune"},
    "Manoj": {"phones": ["9123456780", "9988776655"], "email": "manoj@mail.com", "city": "Delhi"},
    "Zara": {"phones": ["9000011111"], "email": "zara@mail.com", "city": "Pune"},
}


def is_valid_phone(number):
    return number.isdigit() and len(number) == 10


def number_is_registered(number, excluded_contact=None):
    for contact_name, details in contact_records.items():
        if contact_name != excluded_contact and number in details["phones"]:
            return True
    return False


def add_contact():
    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    if name in contact_records:
        print("Contact already exists.")
        return

    phone = input("Enter 10-digit phone number: ").strip()
    if not is_valid_phone(phone):
        print("Phone number must contain exactly 10 digits.")
        return
    if number_is_registered(phone):
        print("This number is already saved.")
        return

    email = input("Enter email: ").strip()
    city = input("Enter city: ").strip()
    contact_records[name] = {
        "phones": [phone],
        "email": email,
        "city": city,
    }
    print("Contact added.")


def add_phone_number():
    name = input("Enter contact name: ").strip()
    if name not in contact_records:
        print("Contact not found.")
        return

    phone = input("Enter another phone number: ").strip()
    if not is_valid_phone(phone):
        print("Phone number must contain exactly 10 digits.")
    elif phone in contact_records[name]["phones"]:
        print("This number is already saved for the contact.")
    elif number_is_registered(phone):
        print("This number belongs to another contact.")
    else:
        contact_records[name]["phones"].append(phone)
        print("Number added.")


def update_contact():
    name = input("Enter contact name: ").strip()
    if name not in contact_records:
        print("Contact not found.")
        return

    print("1. Update email")
    print("2. Update city")
    option = input("Choose an option: ")
    if option == "1":
        contact_records[name]["email"] = input("Enter new email: ").strip()
        print("Email updated.")
    elif option == "2":
        contact_records[name]["city"] = input("Enter new city: ").strip()
        print("City updated.")
    else:
        print("Invalid option.")


def delete_contact():
    name = input("Enter contact name: ").strip()
    if name in contact_records:
        del contact_records[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")


def search_contact():
    print("1. Search by part of a name")
    print("2. Search by phone number")
    option = input("Choose an option: ")

    if option == "1":
        fragment = input("Enter name or part of name: ").lower()
        matches = {
            name: details
            for name, details in contact_records.items()
            if fragment in name.lower()
        }
        if matches:
            for name, details in matches.items():
                print(name, details)
        else:
            print("No matching contact found.")

    elif option == "2":
        phone = input("Enter phone number: ").strip()
        phone_directory = {
            number: name
            for name, details in contact_records.items()
            for number in details["phones"]
        }
        if phone in phone_directory:
            print("Number belongs to:", phone_directory[phone])
        else:
            print("Number not found.")
    else:
        print("Invalid option.")


def display_contact_reports():
    contacts_by_city = {}
    for name, details in contact_records.items():
        contacts_by_city.setdefault(details["city"], []).append(name)

    for names in contacts_by_city.values():
        names.sort()

    print("\nContacts grouped by city:", contacts_by_city)

    contacts_with_extra_numbers = {
        name: details["phones"]
        for name, details in contact_records.items()
        if len(details["phones"]) > 1
    }
    print("\nContacts with multiple numbers:", contacts_with_extra_numbers)

    print("\nPhone directory in alphabetical order:")
    for name in sorted(contact_records):
        print(name, contact_records[name])


def main():
    while True:
        print("\n--- PHONE DIRECTORY ---")
        print("1. Add contact")
        print("2. Add another number")
        print("3. Update email or city")
        print("4. Delete contact")
        print("5. Search")
        print("6. Reports")
        print("7. Exit")

        option = input("Choose an option: ")
        if option == "1":
            add_contact()
        elif option == "2":
            add_phone_number()
        elif option == "3":
            update_contact()
        elif option == "4":
            delete_contact()
        elif option == "5":
            search_contact()
        elif option == "6":
            display_contact_reports()
        elif option == "7":
            print("Program closed.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
