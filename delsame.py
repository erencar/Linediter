def delsame(text):

    beftxt = open(text,"r")
    aftext = open("del-same.txt","w")

    count = 1
    cnt = 0

    bftxt = beftxt.readlines()
    length = len(bftxt)

    for i in range(length):
        line = bftxt[cnt]
        aftext.writelines(line)
        if cnt == length-1:
            break
        else:
            for j in range(count,length):
                if line == bftxt[j]:
                    count=count+1
                else:
                    cnt = count
                    break

    beftxt.close()
    aftext.close()


