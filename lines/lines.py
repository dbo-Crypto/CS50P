import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len (sys.argv) > 2:
     sys.exit("Too many command-line arguments")
else:
    filename = sys.argv[1]
    splited_filename = filename.split(".")
    if splited_filename[1] != "py" or len(splited_filename) != 2:
            sys.exit("Not a Python file")
    count = 0
    try:
        with open(filename) as file:
            lines = file.readlines()
            for line in lines:
                line = line.replace(" ","")
                if line[0] == "\n" or line[0] == "#" or line[0] == " ":
                    count = count
                else:
                    count = count + 1
            print(count)
    except:
        sys.exit("File does not exist")