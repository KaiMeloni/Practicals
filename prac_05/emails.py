def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = name_from_email(email)
        name_check = input("Is your name {}? (Y/n) ".format(name))
        if name_check.upper() != "Y" and name_check != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():  # Loop through dictionary to display emails and names.
        print("{} ({})".format(name, email))


def name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
