

from tokenize import Number
import whois
from multiprocessing.pool import ThreadPool as Pool


class DomainTester:
    def __init__(self,length,word,saveor,nameit) -> None:
        self.klen = length
        self.word = word
        self.saveor = saveor
        self.nameit = nameit
        
    
    def tester(self,dat,count):
        if word == None:
            nword = f'{dat}'
        else:
            nword = f'{word}{dat}'
            nwordr = f'{dat}{word}'
        if len(dat)<6 and "." not in dat and "-" not in dat and Number not in dat:
                try:
                    ndat =whois.whois(f'{nword}.com')
                except:
                    print(f'{nword}.com is available')
                    if self.saveor == "Y":
                        with open(f'{self.nameit}.txt','a') as dt:
                            dt.write(f'{nword}.com\n')
                            
                try:
                    ndat1 = whois.whois(f'{nwordr}.com')
                except:
                    print(f'{nwordr}.com is available')
                    if self.saveor =="Y":
                        with open(f'{self.nameit}.txt','a') as dt:
                            dt.write(f'{nwordr}.com\n')
                print(f'{((count/len(self.chooser()))*100):2f}% Complete')
        
    def chooser(self):
        if self.klen >3 and klen <=5:
            dicti = "dicti/dict.txt"
        elif self.klen<=3:
            dicti = "dicti/text.txt"
        elif self.klen>5:
            dicti = "dicti/2dict.txt"
        elif self.klen== None:
            dicti = "dicti/2dict.txt"
        with open(dicti,"r") as data:
            data = data.read()
            datalist = data.split("\n")
        return datalist
    
    def initailzer(self):
        pool = Pool(128)
        count=0
        for dat in self.chooser():
            count+= 1
            pool.apply_async(self.tester,(dat,count))

        pool.close()
        pool.join()




if __name__ == "__main__":
    saveor = input("Would you like to save results(Y/N) ").capitalize()
    if saveor == "Y":
         nameit = input("Enter Name of file: ")
    else:
        nameit = None
    klen = int(input("Enter Keyword Length:"))
    word = input("Enter word :")

    dm = DomainTester(klen,word,saveor,nameit)
    dm.initailzer()
            
    
            
        

            
