import os

# Directories #
txt = "input.txt"
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

def compile():
    ipt = readTxt()
    write = open(py, "w")
    write.writelines(ipt)
         

def runCode():
    "nothing" 

readTxt()
compile() 
printFile()