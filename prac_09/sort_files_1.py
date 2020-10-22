import shutil
import os

PARENT_DIRECTORY = "FilesToSort"


def main():
    os.chdir(PARENT_DIRECTORY)
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            new_directory = filename.split('.')[-1]
            try:
                os.mkdir(new_directory)
            except FileExistsError:
                pass
            shutil.move(filename, new_directory)


main()