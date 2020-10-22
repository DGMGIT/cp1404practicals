"""
CP1404/CP5632 Practical
Demos of various os module examples
"""

import os

PARENT_DIRECTORY = 'Lyrics'


def main():

    os.chdir(PARENT_DIRECTORY)
    for directory_name, subdirectories, filenames in os.walk('.'):
        # print("Directory:", directory_name)
        # print("\tcontains subdirectories:", subdirectories)
        # print("\tand files:", filenames)
        # print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))

            # full_name = os.path.join(directory_name, filename)
            # new_name = os.path.join(directory_name, get_fixed_filename(filename))
            # os.renames(full_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    enumerate(filename)
    print(filename)
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


main()
