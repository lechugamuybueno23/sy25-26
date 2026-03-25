import glob

files = glob.glob("*.txt") 
#file_name = input("Enter a file name: ")
pattern = input("Enter the pattern to search: ")

for file_name in files:
    file = open(file_name, "r")
    lines = file.readlines()
    file.close()
    for i, line in enumerate(lines):
        if pattern in line:
            print(file_name,i+1,line.strip())
