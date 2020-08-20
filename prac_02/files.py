
# Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.

name = input("Name: ")
out_file = open("name.txt", 'w')
print("{}".format(name), file=out_file)
out_file.close()

# Write code that opens "name.txt" and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file).

in_file = open("name.txt", 'r')
name = in_file.read().strip()
in_file.close()
print("Your name is {}".format(name))

# Create a text file called numbers.txt and save it in your prac_02 directory. Put the following three numbers on separate lines in the file and save it:
# 17
# 42
# 400
# Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result, which should be... 59.

in_file = open("numbers.txt", 'r')
num_1 = int(in_file.readline())
num_2 = int(in_file.readline())
in_file.close()
total_num = num_1 + num_2
print(total_num)

# Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of numbers.

total_lines = 0

in_file = open("numbers.txt", 'r')
for line in in_file:
    total_lines += 1
in_file.close()
print(total_lines)
