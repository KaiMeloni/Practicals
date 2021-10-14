import os


def main():
    file_type_to_category = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        file_type = filename.split('.')[-1]
        if file_type not in file_type_to_category:
            category = input("What category would you like to sort {} files into? ".format(file_type))
            file_type_to_category[file_type] = category
            try:
                os.mkdir(file_type)
            except FileExistsError:
                pass
        os.rename(filename, "{}/{}".format(file_type, filename))


main()
