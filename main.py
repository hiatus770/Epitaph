import os

# Directories #
txt = "io/input.txt"
output = "io/output.txt"
py = "compiled.py"

# Functions #
def readTxt():
    with open(txt, "r") as ipt:
        lines = ipt.readlines() 
        return lines

def printFile(dir = py):
    with open(dir, "r") as ipt:
        lines = ipt.readlines() 
        for line in lines:
            print(line, end = "")
    print()

def compile():
    ipt = readTxt()
    write = open(py, "w")
    for l in ipt:
        if not l.startswith("%"):
            write.write(l)
    

def run():
    os.system("python3 " + py + " > " + output)

# Compiling to a file, Printing the file, and running it to output.txt
compile()
printFile()
run()