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

def splitAlgo(l):
    methods = {}


def run():
    # Variables # 
    ipt = readTxt()
    write = open(py, "w")
    tabCount = 0
    lastTab = 0
    lineCount = 1

    for l in ipt:
        # Keep track of how many lines so far # 
        lineCount = lineCount + 1

# Compiling to a file, Printing the file, and running it to output.txt
printFile()
run()
