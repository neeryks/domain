import whois
saveor = input("Would you like to save results(Y/N) ").capitalize()
if saveor == "Y":
    nameit = input("Enter FileName: ")
klen = int(input("Enter Keyword Length:"))
flist = []
count = 0
if klen ==5:
    dicti = "dict.txt"
elif klen==3:
    dicti = "text.txt"
elif klen==7:
    dicti = "2dict.txt"
with open(dicti,"r") as data:
    data = data.read()
    datalist = data.split("\n")
    word = input("Enter Word:")
    for dat in datalist:
        if len(dat)<7:
            count += 1
            try:
                ndat =whois.whois(f'{word}{dat}.com')
            except:
                print(f'{word}{dat}.com is available')
                with open(f'{nameit}.txt','a') as dt:
                    dt.write(f'{word}{dat}.com\n')
                         
            try:
                ndat1 = whois.whois(f'{dat}{word}.com')
            except:
                print(f'{dat}{word}.com is available')
                with open(f'{nameit}.txt','a') as dt:
                    dt.write(f'{dat}{word}.com\n')
            print(f'{((count/len(datalist))*100):2f}% Complete')
            

            
