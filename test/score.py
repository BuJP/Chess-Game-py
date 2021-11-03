a= ["Aca","0"]
b=["Fgz","1"]
def score(Eblanche, Enoire):
    #verif si il y a deja quelque chose dans le fichier
    with open('test/score.txt','r') as score:
        a=0
        texte=score.readlines()
        if(len(texte)>1):
            a=1

    with open('test/score.txt','a') as score:
        if(a==1):
            print("\n")
            print(Eblanche[0], Eblanche[1],file=score)
            print(Enoire[0], Enoire[1],file=score)
            print("\n-", file=score)
        else:
            print(Eblanche[0], Eblanche[1],file=score)
            print(Enoire[0], Enoire[1]+"\n-",file=score)
            


def affiche_score():
    with open('test/score.txt','r') as score:
        lines = score.readlines()
        lines.reverse()
        print(lines)
        print("Derniere parties :\n")
        i=0

        print("".ljust(51,"-"))
        ligne="|".ljust(3)
        ligne=ligne+"equipe".ljust(20)+"|".ljust(3)
        ligne=ligne+"Pseudo".ljust(9)+"|".ljust(3)
        ligne=ligne+"Score".ljust(12)+"|".ljust(3)
        print(ligne)
        print("".ljust(51,"-"))
        while(i<len(lines)):
            ligne="|".ljust(3)
            x=lines[i].split()
            
            if(x==["--"]):
                print("eze")
                print("".ljust(51,"-"))

            if(x==[] or x== ["-"] ):
                i+=1
                if(i>1):
                    print("".ljust(51,"-"))
            else:
                
                
                
                if(i%4==0):
                    
                    ligne=ligne+"Equipe Blanche".ljust(20)+"|".ljust(3)
                else:
                    ligne=ligne+"Equipe Noire  ".ljust(20)+"|".ljust(3)
                
                ligne=ligne+x[0].ljust(9)+"|".ljust(3)
                
                if(x[1]=="0"):
                    ligne=ligne+"Perdant".ljust(12)+"|".ljust(3)
                elif (x[1]=="1"):
                    ligne=ligne+"Gagnant".ljust(12)+"|".ljust(3)
                else:
                    ligne=ligne+"Match NULL".ljust(12)+"|".ljust(3)
                print(ligne)
            

            i+=1

affiche_score()