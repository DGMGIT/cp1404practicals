import shutil
import os

PARENT_DIRECTORY = "FilesToSort"


def main():
    extension_to_category = {}
    os.chdir(PARENT_DIRECTORY)
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        new_extension = filename.split('.')[-1]
        if new_extension not in extension_to_category:
            category = input("What category would you like to sort {} files into? ".format(new_extension))
            extension_to_category[new_extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass
        shutil.move(filename, extension_to_category[new_extension])


main()