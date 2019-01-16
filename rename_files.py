import os


def rename_files():

    file_list = os.listdir(r'/Users/dcasanova/Pictures/RIL/2-Editadas/ParqueNorte-777-302/')
    os.chdir(r'/Users/dcasanova/Pictures/RIL/2-Editadas/ParqueNorte-777-302/')

    prefix = input("Ingresar prefijo: ")

    for file in file_list:
        # no_digits = []
        # for character in file:
        #     if not character.isdigit():
        #         no_digits.append(character)
        # new_file_name = ''.join(no_digits)
        new_file_name = (prefix + "-" + file).encode('utf-8').strip()
        print(new_file_name)
        os.rename(file, new_file_name)


rename_files()
