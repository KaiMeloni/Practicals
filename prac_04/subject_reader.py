FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    """
    Remove other prints to achieve display 
    such as: [['CP1401', 'Ada Lovelace', 192],['CP1404', 'Alan Turing', 98]]
    """
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)
    input_file.close()
    return data


def subject_details(data):
    """Get print to work, then make it look nice"""
    for subject_data in data:
        print("{} is taught by {:12} and has a {:3} students".format(*subject_data))


main()
