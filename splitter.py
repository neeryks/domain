with open("gjjk.txt","r") as dat:
    dat = dat.read()
    datlist = dat.split("\n")
    for i in datlist:
        if len(i)<=9:
            i = [*i][0:-4]
            if "-" not in i and "." not in i and "&" not in i and "'" not in i:
                with open("fds.txt",'a') as note:
                    i = "".join(i).lower()
                    note.write(f"{i}\n")

