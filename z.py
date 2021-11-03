a= ["Aca","0"]
b=["Fgz","1"]
def score(Eblanche, Enoire):
    #verif si il y a deja quelque chose dans le fichier
    with open('score/score.txt','r') as score:
        a=0
        texte=score.readlines()
        if(len(texte)>1):
            a=1

    with open('score/score.txt','a') as score:
        if(a==1):
            
            print(Eblanche[0], Eblanche[1],file=score)
            print(Enoire[0], Enoire[1],file=score)
            print("\n-", file=score)
        else:
            print(Eblanche[0], Eblanche[1],file=score)
            print(Enoire[0], Enoire[1],file=score)
            print("\n-", file=score)
            


def affiche_score():
    with open('score/score.txt','r') as score:
        lines = score.readlines()
        lines.reverse()
        
        print("Derniere parties :\n")
        i=0
        i2=0

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
                
                
                
                if(i2%2==0):
                    
                    ligne=ligne+"Equipe Noire  ".ljust(20)+"|".ljust(3)
                    i2+=1
                else:
                    ligne=ligne+"Equipe Blanche".ljust(20)+"|".ljust(3)
                    
                    i2+=1

                ligne=ligne+x[0].ljust(9)+"|".ljust(3)
                
                if(x[1]=="0"):
                    ligne=ligne+"Perdant".ljust(12)+"|".ljust(3)
                elif (x[1]=="1"):
                    ligne=ligne+"Gagnant".ljust(12)+"|".ljust(3)
                else:
                    ligne=ligne+"Match NULL".ljust(12)+"|".ljust(3)
                print(ligne)
            

            i+=1
    print("".ljust(51,"-"))

def fg(a):
    a=0
pieceBlanche=[ {"type":"p", "coord":"a2", "reach":[0], "couleur":fg("#FFFFFF") }, {"type":"p", "coord":"b2", "reach":[0], "couleur":fg("#FFFFFF") },{"type":"p", "coord":"c2", "reach":[0], "couleur":fg("#FFFFFF") },{"type":"p", "coord":"d2", "reach":[0], "couleur":fg("#FFFFFF") },{"type":"p", "coord":"e2", "reach":[0], "couleur":fg("#FFFFFF") },{"type":"p", "coord":"f2", "reach":[0], "couleur":fg("#FFFFFF") },{"type":"p", "coord":"g2", "reach":[0], "couleur":fg("#FFFFFF") },{"type":"p", "coord":"h2", "reach":[0], "couleur":fg("#FFFFFF") },
               {"type":"t", "coord":"a1", "reach":[0], "couleur":fg("#FFFFFF") }, {"type":"t", "coord":"h1", "reach":[0], "couleur":fg("#FFFFFF") },
               {"type":"f", "coord":"c1", "reach":[0], "couleur":fg("#FFFFFF") }, {"type":"f", "coord":"f1", "reach":[0], "couleur":fg("#FFFFFF") },
               {"type":"c", "coord":"b1", "reach":[0], "couleur":fg("#FFFFFF") }, {"type":"c", "coord":"g1", "reach":[0], "couleur":fg("#FFFFFF") },
               {"type":"d", "coord":"d1", "reach":[0], "couleur":fg("#FFFFFF") },
               {"type":"r", "coord":"e1", "reach":[0], "couleur":fg("#FFFFFF") }
    
    ]
pieceNoire=[ {"type":"p", "coord":"a7", "reach":[0], "couleur":fg("#000000") }, {"type":"p", "coord":"b7", "reach":[0], "couleur":fg("#000000") },{"type":"p", "coord":"c7", "reach":[0], "couleur":fg("#000000") },{"type":"p", "coord":"d7", "reach":[0], "couleur":fg("#000000") },{"type":"p", "coord":"e7", "reach":[0], "couleur":fg("#000000") },{"type":"p", "coord":"f7", "reach":[0], "couleur":fg("#000000") },{"type":"p", "coord":"g7", "reach":[0], "couleur":fg("#000000") },{"type":"p", "coord":"h7", "reach":[0], "couleur":fg("#000000") },
               {"type":"t", "coord":"a8", "reach":[0], "couleur":fg("#000000") }, {"type":"t", "coord":"h8", "reach":[0], "couleur":fg("#000000") },
               {"type":"f", "coord":"c8", "reach":[0], "couleur":fg("#000000") }, {"type":"f", "coord":"f8", "reach":[0], "couleur":fg("#000000") },
               {"type":"c", "coord":"b8", "reach":[0], "couleur":fg("#000000") }, {"type":"c", "coord":"g8", "reach":[0], "couleur":fg("#000000") },
               {"type":"d", "coord":"d8", "reach":[0], "couleur":fg("#000000") },
               {"type":"r", "coord":"e8", "reach":[0], "couleur":fg("#000000") }
    ]
def savePart(pieceBlanche, pieceNoire,tour):
    with open('score/save.txt','w') as save:
        i=0
        while(i<len(pieceBlanche)):
            x=pieceBlanche[i]
            print(x["type"], x["coord"], file=save)
            i+=1

        i=0
        print("-", file=save)
        while(i<len(pieceNoire)):
            x=pieceNoire[i]
            print(x["type"], x["coord"], file=save)
            i+=1
        print("-",file=save)
        print(tour,file=save)

t=1

a=[]
c=[]
def reloadP(a,c,tour):
    with open('score/save.txt','r') as save:
            lines = save.readlines()
    i=0
    while(i< len(lines)):
        x=lines[i].split()
        
        if(x==[] or x==["-"]):
            
            i+=1
            while(i< len(lines)):
                x=lines[i].split()
                if(x==[] or x==["-"]):
                    i+=1
                    x=lines[i].split()
                    
                    tour=int(x[0])
                    return tour
                    
                else:
                    b={"type":str(x[0]),"coord":str(x[1]), "reach":[0]}
                    c.append(b)
                    i+=1
        else:
            b={"type":str(x[0]),"coord":str(x[1]), "reach":[0]}
            a.append(b)
        i+=1
    





