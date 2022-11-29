from multiprocessing.pool import ThreadPool as Pool
import whois

pool = Pool(128)
li = []

def test(domain,name):
    try:
        domaindat = whois.whois(f"{domain}.com")
    except:
        return
    li.append(f"{domain}.com {domaindat['expiration_date']}")
    return 

def mult(loca):
    with open(f"{loca}","r") as wrt:
        wrt = wrt.read()
        wrtlist = wrt.split("\n")
    for w in wrtlist:
        pool.apply_async(test,(w,"ntest"))
    with open("newr.txt","a") as datee:
        for x in li:
           pool.apply_async(datee.write(f"{x}\n"))
        
    pool.close()
    pool.join() 

mult("dicti/4tst.txt")