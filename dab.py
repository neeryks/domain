import whois
def domain():
    domt = input("Input the Domain:")
    try:
        dom = whois.whois(f"{domt}.com")
        print(f"{domt} is NA")
    except:
        print(f'{domt} is A')
    return 0
while 5>3:
    domain()
