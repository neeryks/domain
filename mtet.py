stri = [*"abcdefghijklmnopqrstuvwxyz"]
for i in stri:
    for j in stri:
        for k in stri:
            for l in stri:
                for m in stri:
                    with open("5txt.txt","a") as ndat:
                        ndat.write(f'{i}{j}{k}{l}{m}\n')

