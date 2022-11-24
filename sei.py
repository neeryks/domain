
from multiprocessing.pool import ThreadPool as Pool
with open("4tstr.txt",'r') as data:
    ddat = data.read()
    dlist = ddat.split("\n")
lis = []
for dat in dlist:
    if dat[0:3].isalpha() or dat[1:4].isalpha():
        lis.append(dat)

dfg = open("dicti/text.txt","r")
dfg = dfg.read()
df = dfg.split("\n")


def finder(li):
    if li[0:3] in df or li[1:4] in df:
        with open("newbase.txt","a") as newdf:
            newdf.write(f"{li}\n")

if __name__ == "__main__":
    pool = Pool(128)
    for li in lis:
        pool.apply_async(finder,(li,))
    
    pool.close()
    pool.join()
    
