from multiprocessing.pool import ThreadPool as Pool
import whois

pool = Pool(128)
li = []

def test(domain,name):
    try:
        domaindat = whois.whois(f"{domain}")
    except:
        return
    li.append(f"{domain} {domaindat['expiration_date']}")
    return 

def mult(loca):
    with open(f"{loca}","r") as wrt:
        wrt = wrt.read()
        wrtlist = wrt.split("\n")
    for w in wrtlist:
        pool.apply_async(test,(w,"ntest"))
    with open("new.txt","a") as datee:
        for x in li:
            datee.write(f"{x}\n")
        
    pool.close()
    pool.join() 

mult("ndat.txt")