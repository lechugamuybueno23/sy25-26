file_name = input("Enter the name of the file to parse(no file txt): ")
file_nme = file_name + ".txt"
file = open(file_nme, "r")

word = input("Enter the word to search for: ")

count = 0

line = file.readline()

while line:
    if word.upper() in line.upper():
        count += line.upper().count(word.upper())
    line = file.readline()

print(f"the word {word} appears {count} amount of times")
