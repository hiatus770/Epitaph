import os
from unicodedata import name

# File Directories #
epi = "io/epitaph.epi"
output = "io/output.txt"

# Variables #
bracketID = 1 
idCnt = 0
var = list() # array keeping track of id to value
names = dict() # dict keeping track of name to id
nameTracker = set() # keeps track of built variables

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

def accumulate(text, lineNumber):

    # variables # 
    global var  # array keeping track of id to value
    global names  # dict keeping track of name to id
    global nameTracker  # keeps track of built variables

    # result list # 
    result = list()

    # remove spaces # 
    # text = text.replace(" ", "", -1)
    
    # Split by operator # 
    lastOperator = 0
    for i in range(0, len(text)): 
        print(i, text[i])
        if text[i] == "+" or  text[i] == "-" or text[i] == "/" or text[i] == "*":
            print(lastOperator, i)
            if text[lastOperator:i] != "":
                result.append(text[lastOperator:i])
            result.append(text[i])
            lastOperator = i+1
        elif i == len(text)-1:
            result.append(text[lastOperator:len(text)])
    
    # multiplication and subtraction bedmas order # 
    md = list()
    sa = list()

    for i in range(len(result)):
        if result[i] == "*" or result[i] == "/":
            md.append(i)
        if result[i] == "+" or result[i] == "-":
            sa.append(i)

    for i in range(len(result)):
        obj = result[i]
        if obj.isdigit():
            result[i] = int(obj)
        elif obj.isalpha():
            print("VARS/STRINGS: ", obj)
            if not obj.startswith('"'):
                if obj in nameTracker:
                    result[i] = var[names[obj]]
                else:
                    print("ERROR ON LINE", lineNumber, obj, "WAS NOT DEFINED")


    print("Accumulated:", result)


# Will split line into methods and does matter when "", {} and () are present #
def splitAlgo(l):
    methods = list()
    cnt = 0

    if len(l) > 1:
        endcount = 1
        lastStop = 0
        while (cnt < len(l)):
            if l[cnt] == "(":
                # find another ) and then mogus the sogus
                if (l.find(")", cnt+1) != -1):
                    cnt = l.find(")", cnt+1)
            if l[cnt] == '"':
                # find another ) and then mogus the sogus
                if (l.find('"', cnt+1) != -1):
                    cnt = l.find('"', cnt+1)
            if l[cnt] == " ":
                endcount = endcount + 1 
                # if reahc space increase endcount value, when endcount is two then splice a lice
            if endcount == 2 and l[lastStop:cnt] != "":
                # encountered another space
                endcount = 1
                methods.append(l[lastStop:cnt])
                lastStop = cnt+1
            if cnt == len(l)-1 and endcount == 1:
                # we have reached the end of the string
                methods.append(l[lastStop:len(l)])
                break; 
            cnt = cnt + 1
    else:
        methods.append(l)

    print(methods)
    return methods

# merges elements in a list # 
def merge(lines, a, b):
    result = ""
    for i in range(a+1, b):
        print(i)
        lines[a] = str(lines[a]) + str(lines[i]) 
    return lines[a]; 


# Runs entire code # 
def run():
    # Variables # 
    ipt = readTxt()
    lineCount = 1
    global idCnt

    global var  # array keeping track of id to value
    global names  # dict keeping track of name to id
    global nameTracker  # keeps track of built variables


    for l in ipt: 
        # Line count for errors #
        lineCount = lineCount + 1
        line = splitAlgo(l)
        
        if len(line) >= 4:
            if line[0] == "%" and line[2] == "=":
                if line[1] in nameTracker:
                    print("VARIABLE ALREADY CREATED")
                    text = str(merge(line, 3, len(line)))
                    accumulate(text, lineCount)
    
                else:
                    # this means the variable will be created!!!
                    var.append(line[3])
                    names[line[1]] = idCnt 
                    nameTracker.add(line[1])
                    idCnt = idCnt + 1 
    
    # print(var)
    # print(names)
    # print(nameTracker)







# Compiling to a file, Printing the file, and running it to output.txt
run()
