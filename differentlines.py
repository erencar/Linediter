def dif(first,second):

    firstt = open(first,"r")
    secont = open(second,"r")
    result = open("different-lines.txt","w")

    txt1 = firstt.readlines()
    txt2 = secont.readlines()

    count = 0
    length1 = len(txt1)
    length2 = len(txt2)

    for i in range(length1):
        difline = txt1[i]
        for j in range(length2):
            if difline != txt2[j]:
                count = count + 1
                if count == length2:
                        result.writelines(difline)
                        count = 0
            else:
                count = 0
                break

    for i in range(length2):
        difline = txt2[i]
        for j in range(length1):
            if difline != txt1[j]:
                count = count + 1
                if count == length1:
                        result.writelines(difline)
                        count = 0
            else:
                count = 0
                break

    firstt.close()
    secont.close()
    result.close()


