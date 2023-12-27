import pyfiglet
import sys


#Main program loop
def main():
    while True:
        try:
            contact_list = pyfiglet.figlet_format("Contacts Program", font="big")
            print(contact_list)
            print("1. Add a contact")
            print("2. List all contacts")
            print("3. Search for a contact")
            print("4. Delete a contact")
            print("5. Quit")

            choice = input("Enter your choice (1/2/3/4/5): ")
            print()
            if choice == '1':
                add_contact()
                print()
            elif choice == '2':
                list_contacts()
                print()
            elif choice == '3':
                search_contact()
                print()
            elif choice == '4':
                delete_contact()
                print()
            elif choice == '5':
                goodbye = pyfiglet.figlet_format("Goodbye!", font="big")
                print(goodbye)
                print()
                break
            else:
                print("Invalid choice. Please enter a valid option (1/2/3/4/5).")
                print()
        except EOFError:
            print()
            sys.exit("Exiting the program...")
        except KeyboardInterrupt:
            print()
            sys.exit("Exiting the program...")

#Dictionary to store contacts with names as keys and details as values
contacts = {}

# Function to add a contact
def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")

    contacts[name] = {
        "Phone": phone,
        "Email": email
    }
    print()
    print(f"{name} has been added to your contacts!")

#Function to display all contacts
def list_contacts():
    print()
    print("Contacts List:")
    for name, details in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {details['Phone']}")
        print(f"Email: {details['Email']}")

#Function to search for a contact
def search_contact():
    name = input("Enter the name to search: ")
    if name in contacts:
        details = contacts[name]
        print(f"Name: {name}")
        print(f"Phone: {details['Phone']}")
        print(f"Email: {details['Email']}")
    else:
        print(f"{name} not found in your contacts.")

#Function to delete a contact
def delete_contact():
    name = input("Enter the name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"{name} has been deleted from your contacts.")
    else:
        print(f"{name} not found in your contacts.")



if __name__ == "__main__":
    main()

