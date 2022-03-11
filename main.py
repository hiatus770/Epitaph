import os

# File Directories #
txt = "io/input.txt"
output = "io/output.txt"

# Returns all lines from the file #
def readTxt():
    with open(txt, "r") as ipt:
        lines = ipt.readlines() 
        return lines

# Prints out the output of said program # 
def printFile(dir = output): 
    with open(dir, "r") as ipt:
        lines = ipt.readlines() 
        for line in lines:
            print(line, end = "")
    print()

# Will split line into methods #
def splitAlgo(l):
    methods = {}

# Executes a line of code # 
def executeCode(code):
    "Literally just run one line, how hard could it be :skull:"

# Loop #
def loop(idk):
    "I really dont know :("

# If statement # 
def ifS(idk):
    "I also dont know"

# Runs entire code # 
def run():
    # Variables # 
    ipt = readTxt()
    lineCount = 1

    var = {} # array keeping track of id to value
    names = {} # dict keeping track of name to id

    for l in ipt: 
        # Line count for errors #
        lineCount = lineCount + 1

        # check if its a loop

# Compiling to a file, Printing the file, and running it to output.txt
printFile()
run()
