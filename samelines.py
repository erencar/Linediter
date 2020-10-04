def same(first,second):

    firstt = open(first,"r")
    secont = open(second,"r")
    result = open("same-lines.txt","w")

    txt1 = firstt.readlines()
    txt2 = secont.readlines()

    length1 = len(txt1)
    length2 = len(txt2)

    for i in range(length1):
        sameline = txt1[i]
        for j in range(length2):
            if sameline == txt2[j]:
                result.writelines(sameline)
                break
    firstt.close()
    secont.close()
    result.close()