from multiprocessing.pool import ThreadPool as Pool
import whois
##testing all 4 letter words in domain system agaist good extensions##
def testercom(wrd):
    try:
        do = whois.whois(f'{wrd}.com')
    except:
        with open("5tstr.txt",'a') as wrt:
            wrt.write(f'{wrd}.com\n')

def testernet(wrd):
    try:
        do = whois.whois(f'{wrd}.net')
    except:
        with open("4tstr.txt",'a') as wrt:
            wrt.write(f'{wrd}.net\n')

def testerorg(wrd):
    try:
        do = whois.whois(f'{wrd}.org')
    except:
        with open("4tstr.txt",'a') as wrt:
            wrt.write(f'{wrd}.org\n')

if __name__=="__main__":
    pool = Pool(128)
    count = 0
    with open("5txt.txt","r") as wrdlster:
        nwrdlst = wrdlster.read()
        wrdlst = nwrdlst.split("\n")
        for wrd in wrdlst:
            pool.apply_async(testercom,(wrd,))
            #pool.apply_async(testernet,(wrd,))
            #pool.apply_async(testerorg,(wrd,))
            count += 1
            print(f'{((count/11881376)*100):2f}% Complete')
    
    pool.close()
    pool.join() 



