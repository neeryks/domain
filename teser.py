
import whois

with open("2dict.txt","r") as data:
    cn = 0 
    count = 0
    data1 = data.read()
    wlist = data1.split("\n")
    for domain in wlist[20312:100000]:
        count += 1
        tcount = (count/len(wlist[50000:100000]))*100
        print(f'{tcount:2f}% Completed [{count}]')
        if len(domain)<8 and domain.isalpha():
            try:
                det = whois.whois(f'{domain}.com')
            except:
                try:
                    det = whois.whois(f'{domain}.com')
                except:
                        with open("avail.txt","a") as wri:
                            cn += 1
                            print(f'Adding {domain}.com Total:{cn}')
                            wri.write(f'{domain}.com\n')
