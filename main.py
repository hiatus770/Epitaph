import os
import sys

# System argument information # 
fileOutput = False
run = True
args = sys.argv 
db = False 

# File Directories #
epi = "io/epitaph.epi"
output = "TERMINAL"

# Main argument logic # 
for i in args:
    if len(args) == 2:
        if i == "-h" or i == "--help":
            msg = """
            \t\t\tHELP

            Specify output file by providing a file that starts with output. or it will default to terminal

            Specify the input file for the esolang for a file that ends with .epi

            Example arguments: directory/esolangFile.epi directory/output.txt 
            
            """
            print(msg)
            run = False 
        if i == "-g" or i == "--git":
            print("https://github.com/hiatus770/Epitaph")
            run = False 
    if i == "-d" or i == "--debug":
        db = True 
    if i.endswith(".epi"):
        epi = i
    if i.endswith(".txt"):
        output = i

# Print out the file directories # 
print("OUTPUT DIRECTORY: ", output)
print("INPUT DIRECTORY: ", epi)

# Variables #
idCnt = 0 # The id count for all the variables 
var = list() # array keeping track of id to value
names = dict() # dict keeping track of name to id
nameTracker = set() # keeps track of built variables
bracketID = 0
true = 0
false = 1
ipt = ""
debugList = list()
outputList = list()

# Clear the output file before printing out anything
with open(output, "w") as clear:
    clear.write("")

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

# takes in a string and gives it a value !!!
def accumulate(text, lineNumber=69.420):

    # variables # 
    global var  # array keeping track of id to value
    global names  # dict keeping track of name to id
    global nameTracker  # keeps track of built variables

    # result list # 
    result = list()

    # Split by operator # 
    lastOperator = 0
    for i in range(0, len(text)): 
        if text[i] == "+" or  text[i] == "-" or text[i] == "/" or text[i] == "*" or text[i] == ",":
            if text[lastOperator:i] != "":
                result.append(text[lastOperator:i])
            result.append(text[i])
            lastOperator = i+1
        elif i == len(text)-1:
            result.append(text[lastOperator:len(text)])
    
    for i in range(len(result)):
        if not result[i].startswith('"'):
            result[i] = result[i].replace(" ", "", -1)

    # multiplication and subtraction bedmas order # 
    md = list()
    sa = list()

    # Converting ints to ints and strings leaving them as they are and finding variables
    for i in range(len(result)):
        obj = result[i]
        if obj.isdigit():
            result[i] = int(obj)
        elif type(obj) == str:
            if not obj.startswith('"'):
                if obj in nameTracker:
                    result[i] = var[names[obj]]

    # make sure whatever you append is an int and not a string :/
    for i in range(len(result)):
        if result[i] == "*" or result[i] == "/":
            if type(result[i-1]) == int or type(result[i-1]) == float and type(result[i+1]) == int or type(result[i+1]) == float:
                md.append(i)

    #print("PERFORMING BEDMAS ON: ", result)

    cnt = 0 
    err = 0

    # do all * / parts of accumulate # 
    while(len(md)!=0):
        if (result[md[0]-err]=="/"):
            result[md[0]-err] = result[md[0]-1-err] / result[md[0]+1-err]
            del result[md[0]-1-err]
            del result[md[0]-err]
            del md[0]
            err = err + 2
        else:
            result[md[0]-err] = result[md[0]+1-err] * result[md[0]-1-err]
            del result[md[0]-1-err]
            del result[md[0]-err]
            del md[0]
            err = err + 2

    for i in range(len(result)):
        if result[i] == "+" or result[i] == "-":
            if type(result[i-1]) == int or type(result[i-1]) == float and type(result[i+1]) == int or type(result[i+1]) == float:
                sa.append(i)

    # reset error # 
    err = 0

    # do all +/- parts of accumulate # 
    while(len(sa)!=0):
        if (result[sa[0]-err]=="+"):
            result[sa[0]-err] = result[sa[0]+1-err] + result[sa[0]-1-err]
            del result[sa[0]-1-err]
            del result[sa[0]-err]
            del sa[0]
            err = err + 2
        else:
            result[sa[0]-err] = result[sa[0]+1-err] - result[sa[0]-1-err]
            del result[sa[0]-1-err]
            del result[sa[0]-err]
            del sa[0]
            err = err + 2
    
    debug("ACCUMULATED:" + str(result) + "\n")
    return result

# Will split line into methods and does matter when "", {} and () are present #
def splitAlgo(l):
    methods = list()
    cnt = 0

    if len(l) > 1:
        endcount = 1
        lastStop = 0
        while (cnt < len(l)):
            if l[cnt] == "(":
                # find another ) 
                if (l.find(")", cnt+1) != -1):
                    cnt = l.find(")", cnt+1)
            if l[cnt] == '"':
                # find another ) and then mogus the sogus
                if (l.find('"', cnt+1) != -1):
                    cnt = l.find('"', cnt+1)
            if l[cnt] == " ":
                endcount = endcount + 1 
                # if reahc space increase endcount value, when endcount is two then splice a lice
            if endcount == 2: #and l[lastStop:cnt] != "":
                # encountered another space
                endcount = 1
                methods.append(l[lastStop:cnt])
                lastStop = cnt+1
            if cnt == len(l)-1 and endcount == 1:
                # we have reached the end of the string
                methods.append(l[lastStop:len(l)])
                break; 
            cnt = cnt + 1
        err = 0
        for i in range(len(methods)):
            if methods[i-err] == "": 
                del methods[i-err]
                err = err + 1
    else:
        methods.append(l)
    return methods

# merges elements in a list # 
def merge(lines, a, b):
    result = ""
    for i in range(a+1, b):
        lines[a] = str(lines[a]) + str(lines[i]) 
    return lines[a]; 

# prints something to output.txt
def toOutput(info):
    for i in info:
        i = str(i)
        i = i.replace('"', "", -1)
        i = i.replace(",", " ", -1)
        outputList.append(str(i))

# debug? # 
def debug(info):
    debugList.append(str(info))

# The print statement of Epitaph # 
def etch(line):
    opening = line.find("(")
    closing = line.find(")")
    inBracket = line[opening+1:closing]
    acc = accumulate(inBracket)
    toOutput(acc)

# Getting input for epitaph # 
def fetch(cmd):

    ### GLOBAL VARIABLES ### 
    global bracketID 
    global idCnt 
    global var  
    global names
    global nameTracker      

    openingBracket = cmd.find("(")
    closingBracket = cmd.find(")")
    varName = cmd[openingBracket+1:closingBracket]
    if varName in nameTracker:
        var[names[varName]] = input()
    elif varName not in nameTracker:
        names[varName] = idCnt 
        nameTracker.add(varName)
        var.append(accumulate(input())[0])
        idCnt = idCnt + 1 

# Determines if input is true (0) or false (1) # 
def truFalse(text):
    debug("EVALUATING: " + text) 

    # variables # 
    global var  # array keeping track of id to value
    global names  # dict keeping track of name to id
    global nameTracker  # keeps track of built variables

    # result list # 
    result = list()

    # Split by operator # 
    lastOperator = 0
    for i in range(0, len(text)): 
        if text[i] == "!" or text[i] == "=" or text[i] == "<" or text[i] == ">":
            if text[lastOperator:i] != "":
                result.append(text[lastOperator:i])
            result.append(text[i])
            lastOperator = i+1
        elif i == len(text)-1:
            result.append(text[lastOperator:len(text)])
    
    for i in range(len(result)):
        if not result[i].startswith('"'):
            result[i] = result[i].replace(" ", "", -1)

    md = list()
    cnt = 0 
    err = 0

    for i in range(len(result)):
        obj = result[i]
        if obj.isdigit():
            result[i] = int(obj)
        elif type(obj) == str:
            if not obj.startswith('"'):
                if obj in nameTracker:
                    result[i] = var[names[obj]]

    # find all == != < >
    for i in range(len(result)):
        if result[i] == "<"  or result[i] == ">" or result[i] == "=" or result[i] == "!":
            if type(result[i-1]) == int or type(result[i-1]) == float and type(result[i+1]) == int or type(result[i+1]) == float or type(result[i-1]) == str and type(result[i+1]) == str:
                md.append(i)


    # do all * / parts of accumulate # 
    while(len(md)!=0):
        if (result[md[0]-err]=="="):
            if result[md[0]-1-err] == result[md[0]+1-err]:
                # set to true
                result[md[0]-err] = 0
            else:
                # set to false
                result[md[0]-err] = 1
            del result[md[0]-1-err]
            del result[md[0]-err]
            del md[0]
            err = err + 2
        elif (result[md[0]-err]=="!"):
            if result[md[0]-1-err] != result[md[0]+1-err]:
                # set to true
                result[md[0]-err] = 0
            else:
                # set to false
                result[md[0]-err] = 1
            del result[md[0]-1-err]
            del result[md[0]-err]
            del md[0]
            err = err + 2
        elif (result[md[0]-err]==">"):
            if result[md[0]-1-err] > result[md[0]+1-err]:
                # set to true
                result[md[0]-err] = 0
            else:
                # set to false
                result[md[0]-err] = 1
            del result[md[0]-1-err]
            del result[md[0]-err]
            del md[0]
            err = err + 2
        elif (result[md[0]-err]=="<"):
            if result[md[0]-1-err] < result[md[0]+1-err]:
                # set to true
                result[md[0]-err] = 0
            else:
                # set to false
                result[md[0]-err] = 1
            del result[md[0]-1-err]
            del result[md[0]-err]
            del md[0]
            err = err + 2

    debug("TRUE OR FALSE STATEMENT: " + str(result))
    if result == [0]:
        return 0
    else:
        return 1

# If statement thing for esolang # 
def ifStatement(line, startIf, endIf):
    code = list()

    debug("IF statement starts at " + str(startIf) + " Ends at " + str(endIf))

    for i in range(startIf+1, endIf):
        # print("APPENDING", i)
        code.append(ipt[i])


    openingBracket = line.find("(")
    closingBracket = line.find(")")
    condition = truFalse(line[openingBracket+1:closingBracket])

    if condition == 0:
        debug("Running code: " + str(code))
        runChunk(code, startIf)

# While loop! # 
def whileLoop(line, start, end):
    code = list()

    openingBracket = line.find("(")
    closingBracket = line.find(")")
    condition = truFalse(line[openingBracket+1:closingBracket])

    for i in range(start+1, end):
        # print("APPENDING", i)
        code.append(ipt[i])
    
    debug("While loop from: "+ str(start) + " " + str(end))

    while condition == 0:
        runChunk(code, start)   
        condition = truFalse(line[openingBracket+1:closingBracket])     
    
# Make sure this is updated to run constantly or else if statements will be kinda wackilicious # 
def runChunk(code, lineIndex):
    global bracketID # bracket id moment!!!
    global idCnt # some idcnt for var
    global var  # array keeping track of id to value
    global names  # dict keeping track of name to id
    global nameTracker  # keeps track of built variables
    
    lineCount = lineIndex

    debug("Running lines: \n"+ str(code) + "\nStarting at line " + str(lineCount+1))


    while lineCount < len(ipt)-1: 
        # Line count for errors #
        lineCount = lineCount + 1
        l = ipt[lineCount]
        l = l.replace("\n", "", -1)
        line = splitAlgo(l)

        isNotComment = True 
        if l.startswith("%") and l.endswith("%"):
            isNotComment =  False
        else:
            debug(str(line))

        if len(line) >= 3 and isNotComment:
            if line[1] == "=" and line[0] in nameTracker:
                #  Assigning a value 
                debug("ASSIGNMENT:" + str(l))
                text = str(merge(line, 2, len(line)))
                varID = names[line[0]] 
                var[varID] = accumulate(text, lineCount)[0]

            elif line[1] == "=" and line[0] not in nameTracker:
                # Creation of a new variable # 
                debug("CREATION OF: " + str(line[0]) + " ON LINE " + str(lineCount))
                text = str(merge(line, 2, len(line)))
                dataList = accumulate(text, lineCount)
                debug(str(dataList))
                data = ""
                if len(dataList) > 1:
                    debug("INVALID VARIABLE")
                else:
                    data = dataList[0] 
                var.append(data)
                debug("VALUE OF " + str(line[0]) + " IS " + str(data))
                names[line[0]] = idCnt 
                nameTracker.add(line[0])
                idCnt = idCnt + 1 

        if not line == []:
            if line[0].replace(" ", "").startswith("etch") and isNotComment:
                debug("ETCH FOUND!")
                etch(line[0])

            if line[0].replace(" ", "").startswith("fetch") and isNotComment: 
                debug("FETCH FOUND")
                fetch(line[0])

            if line[0].startswith("if") and isNotComment: 
                debug("IF STATEMENT")
                debug(line)
                ifLine = merge(line, 0, len(line))
                ifState = lineCount # where the if statement starts
                ifEnd = lineCount
                debug("IF LINE: " + str(ifLine))
                for i in range(lineCount, len(ipt)):
                    debug("LOOKING FOR }"+ifLine[len(ifLine)-1])
                    q = ipt[i].replace(" ", "")
                    q = q.replace("\n", "")
                    #print(q)
                    if (q == "}"+ifLine[len(ifLine)-1]):
                        debug("FOUND CLOSING BRACKET FOR IF: " + str(i))
                        ifEnd = i
                        lineCount = i
                        break; 

                ifStatement(ifLine, ifState, ifEnd)

            if line[0].startswith("while") and isNotComment: 
                debug("WHILE LOOP")
                debug(line)
                whileLine = merge(line, 0, len(line))
                whileState = lineCount # where the if statement starts
                whileEnd = lineCount
                #print("IF LINE: ", ifLine)
                for i in range(lineCount, len(ipt)):
                    debug("LOOKING FOR }"+whileLine[len(whileLine)-1])
                    q = ipt[i].replace(" ", "")
                    q = q.replace("\n", "")
                    #print(q)
                    if (q == "}"+whileLine[len(whileLine)-1]):
                        whileEnd = i
                        lineCount = i
                        break; 


                whileLoop(whileLine, whileState, whileEnd)

# Assigns all the bracket ID's in the code for code moment! # 
def bracketAssign():
    global bracketID 
    debug("ASSIGNING BRACKET ID")
    bracketID = 0
    cnt = 0
    while cnt < len(ipt):
        q = ipt[cnt].replace(" ", "")
        q = ipt[cnt].replace("\n", "")
        if q.endswith("{"):
            bracketID = bracketID + 1
            ipt[cnt] = ipt[cnt].replace("\n", "").replace(" ", "")+str(bracketID)
        elif q.startswith("}") or q.endswith("}"):
            ipt[cnt] = ipt[cnt].replace("\n", "").replace(" ", "")+str(bracketID)
            bracketID = bracketID - 1
        cnt = cnt + 1 
    debug("Assigned: " + str(ipt))

# Initiates the code and runs the .epi file # 
def main():
    # Variables # 
    global ipt
    ipt = readTxt()
    lineCount = -1
    bracketAssign() 
    global bracketID # bracket id moment!!!
    global idCnt # some idcnt for var
    global var  # array keeping track of id to value
    global names  # dict keeping track of name to id
    global nameTracker  # keeps track of built variables
    runChunk(ipt, -1)

if run:
    main()
if output != "TERMINAL" and run == True:
    with open(output, "w") as opt:
        opt.writelines(outputList)
        opt.write("\n\n")
        if db:
            opt.writelines(debugList)
elif run:
    print("\n\t\tOUTPUT")
    for i in outputList:
        print(i)
    if db: # db is debug boolean
        print("\n\t\tDEBUG")
        for i in debugList: 
            print(i)
