# ShAME THIS CODE!!! # 

for i in range(len(l)):
    if len(l) == 1:
        methods.append(l)
        break
    if l[i] == " " or i == 0 and l != "\n":
        cnt = i + 1
        while l[cnt] != " ":
            print(l[cnt], i, cnt)
            if (cnt == len(l)-1):
                cnt = len(l)
                break
            if (l[cnt] == "("):
                cnt = l.find(")", cnt)
                if (cnt == -1):
                    cnt = len(l)-1
            cnt = cnt + 1
        if (cnt == len(l)):
            break
        if (l[i:cnt] != " ") and i == 0:
            methods.append(l[i:cnt])
        elif (l[i:cnt] != " "):
            methods.append(l[i+1:cnt])
    if (cnt == len(l)):
        break