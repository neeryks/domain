import whois
string = [*"abcdefghijklmnopqrstuvwxyz"]
string1 = [*"qrst"]
count = 0
cn =0
for i in string1:
    for j in string:
        for k in string:
            for l in string:
                domain = f'{i}{j}{k}{l}'
                count += 1
                tcount = (count/456976)*100
                print(f'{tcount:2f}% Completed [{count}]')
                if len(domain)<8 and domain.isalpha():
                    try:
                        det = whois.whois(f'{domain}.com')
                    
                    except:
                        with open("availter.txt","a") as wri:
                            cn += 1
                            print(f'Adding {domain}.com Total:{cn}')
                            wri.write(f'{domain}.com\n')
