import os

# File Directories #
epi = "io/epitaph.epi"
output = "io/output.txt"

# Returns all lines from the file #
def readTxt():
    with open(epi, "r") as ipt:
        lines = ipt.readlines() 
        return lines

# Prints out the output of compiled program # 
def printFile(dir = output): 
    with open(dir, "r") as ipt:
        lines = ipt.readlines() 
        for line in lines:
            print(line, end = "")
    print()

# Will split line into methods and does matter when "", {} and () are present #
def splitAlgo(l):
    methods = list()
    cnt = 0
    for i in range(len(l)):
        if len(l) == 1:
            methods.append(l)
            break
        if l[i] == " " or i == 0 and l != "\n":
            cnt = i+1
            while l[cnt] != " ":
                cnt = cnt + 1
                if (l[cnt] == "("):
                    cnt = l.find(")", cnt)
                if (l[cnt] == "{"):
                    cnt = l.find("}", cnt)
                    if (cnt == -1):
                        cnt = len(l)-1
                if (l[cnt] == '"'):
                    cnt = l.find('"', cnt+1)
                if (cnt == len(l)-1):
                    cnt = len(l)
                    break
            if (l[i:cnt] != " ") and i == 0:
                methods.append(l[i:cnt])
            elif (l[i:cnt] != " "):
                methods.append(l[i+1:cnt])
        if (cnt == len(l)):
            break
    print(methods)

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
        splitAlgo(l)






# Compiling to a file, Printing the file, and running it to output.txt
run()
