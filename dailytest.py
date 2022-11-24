
import whois
from multiprocessing.pool import ThreadPool as Pool
saveor = input("Would you like to save results(Y/N) ").capitalize()
if saveor == "Y":
    nameit = input("Enter FileName: ")
klen = int(input("Enter Keyword Length:"))
flist = []
count = 0
if klen ==5:
    dicti = "dicti/dict.txt"
elif klen==3:
    dicti = "dicti/text.txt"
elif klen==7:
    dicti = "dicti/2dict.txt"
with open(dicti,"r") as data:
    data = data.read()
    datalist = data.split("\n")
    word = input("Enter Word:")
pool_size = 128
def tester(dat,count):
    if len(dat)<7:
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

pool = Pool(pool_size)

for dat in datalist:
    count+= 1
    pool.apply_async(tester,(dat,count))

pool.close()
pool.join()

            
        

            
