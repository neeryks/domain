with open("avail.txt","r") as data:
    data1 = data.read()
    data1 = data1.split("\n")
    for dat in data1:
        if len(dat) <= 9:
            print(dat)