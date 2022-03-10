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

    for cnt in range(len(l)):
        i = l[cnt]
        if i == '"':
            quoteFind = cnt
            while(true):
                if (l[quoteFind] == '"'):
                    break;  
                else: 
                    quoteFind = quoteFind + 1
        elif i == " ":
            "Baba booey"

def compile():
    # Variables # 
    ipt = readTxt()
    write = open(py, "w")
    tabCount = 0
    lastTab = 0
    lineCount = 1

    for l in ipt:
        # Keep track of how many lines so far # 
        lineCount = lineCount + 1

        # If it is not a comment then proceed # 
        if not l.startswith("%") and not l.endswith("%"):

            # Splitting algo makes sure strings are not split :)
            lines = splitAlgo(l)

            # Tab count stuff
            lastTab = tabCount
            for i in l:
                if i == "{":
                    tabCount = tabCount + 1
                if i == "}": 
                    tabCount = tabCount - 1
                    lastTab = tabCount
            l = l.replace("{", "", -1)
            l = l.replace("}", "", -1)
            
            # method finder
            print("Methods Found: ")
            
            # Dont print anything if it is only curly brackets
            if l != "{" or l != "}":
                write.write(((lastTab) * "    ") + l)
    

def run():
    os.system("python3 " + py + " > " + output)

# Compiling to a file, Printing the file, and running it to output.txt
compile()
printFile()
run()