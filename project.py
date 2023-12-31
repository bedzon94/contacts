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

            choice = input("Enter your choice (1/2/3/4/5): \n")
            if choice == '1':
                print(add_contact())
            elif choice == '2':
                print(list_contacts())
            elif choice == '3':
                search_contact()
            elif choice == '4':
                delete_contact()
            elif choice == '5':
                goodbye = pyfiglet.figlet_format("Goodbye!\n", font="big")
                print(goodbye)
                break
            else:
                print("Invalid choice. Please enter a valid option (1/2/3/4/5).\n")
        except EOFError:
            sys.exit("\nExiting the program...")
        except KeyboardInterrupt:
            sys.exit("\nExiting the program...")

#Dictionary to store contacts with names as keys and details as values
contacts = {}

#Function to add a contact
def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")

    contacts[name] = {
        "Phone": phone,
        "Email": email
    }
    print()
    return f"{name} has been added to your contacts!"

#Function to display all contacts
def list_contacts():
    result = "\nContacts List: \n"
    for key, value in contacts.items():
        result += f"\n{key.capitalize()}: {value}"
    return result


#Function to search for a contact
def search_contact():
    name = input("Enter the name to search: \n")
    if name in contacts:
        details = contacts[name]
        print(f"Name: {name}")
        print(f"Phone: {details['Phone']}")
        print(f"Email: {details['Email']}\n")
    else:
        print(f"{name} not found in your contacts.\n")

#Function to delete a contact
def delete_contact():
    name = input("Enter the name to delete: \n")
    if name in contacts:
        del contacts[name]
        print(f"{name} has been deleted from your contacts.\n")
    else:
        print(f"{name} not found in your contacts.\n")



if __name__ == "__main__":
    main()

