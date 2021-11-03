from pions import initCoordPieceB,initCoordPieceN,initpiece2
from plateaux import ech
from coup import verifVictoire, deplacementBot, deplacementm
from colored import fg, bg, attr
from affichage import affiche_plateau, affiche_plateau_reach,reverseAffiche_plateau
import os
from z import score, affiche_score, reloadP, savePart


res = attr('reset')


start = 1

while(start==1):
    if(ech!= ["0"]*64):
        ech=["0"]*64
    
    


    
    


    os.system("cls")    
    print(fg("#00D7FA")+"--------- MENU PRINCIPAL ---------\n\n"+res)
    menu = 0
    while(menu != 1 and menu != 2 and menu != 3 and menu != 4 and menu != 5  ):
        print(fg("#00D7FA")+"1-"+res+fg("#FFA07A")+" JOUER A DEUX\n"+res+fg("#00D7FA")+"2-"+res+fg("#FFA07A")+" JOUER CONTRE L'ORDINATEUR\n"+res+fg("#00D7FA")+"3-"+res+fg("#FFA07A")+" CHARGER LA PARTIE PRECEDENTE \n"+res+fg("#00D7FA")+"4-"+res+fg("#FFA07A")+" TABLEAU DES SCORES\n"+res+fg("#00D7FA")+"5-"+res+fg("#FFA07A")+" QUITTER"+res )
        menu = int(input(fg("#FF0000")+"-> "+res))


    if (menu ==1 or menu == 3):
        tour=0
        last=""
        if(menu==3):
            pieceBlanche=[]
            pieceNoire=[]
            tour=reloadP(pieceBlanche,pieceNoire, tour)
            ech=initpiece2(ech,pieceBlanche,pieceNoire)
            if (tour%2 == 0):
                affiche_plateau(ech,pieceBlanche, pieceNoire,last)
            else:
                reverseAffiche_plateau(ech,pieceBlanche, pieceNoire,last)
                        
            
            
        else:
            pieceBlanche = initCoordPieceB()
            pieceNoire = initCoordPieceN()
            
        
        

        victoire = 0
        test = True
        pseudoBlanche=input(fg("#00D7FA")+"Equipe Blanche "+res+"| "+fg("#FFA07A")+"Entrez votre pseudo : "+res)
        pseudoNoire=input(fg("#00D7FA")+"Equipe Noire "+res+fg("#808080")+"| "+res+fg("#FFA07A")+"Entrez votre pseudo : "+res)
        while(victoire == 0):
            
            if(tour > 0):
                
                #demande si ils veulent continuer la partie
                choix = 0
                while(choix != 1 and choix != 2 ):
                    print(fg("#00D7FA")+"1-"+res+fg("#FFA07A")+" CONTINUER LA PARTIE\n"+res+fg("#00D7FA")+"2-"+res+fg("#FFA07A")+" QUITTER LA PARTIE"+res)
                    choix = int(input())
                if( choix == 2):
                    victoire = -1
                    test = False
                

            os.system("cls")

            if(test==True):
                if (tour%2 == 0):
                    print(fg("#FFA07A")+"--------------- TOUR DE "+pseudoBlanche+" ---------------\n"+res)
                else:
                    print(fg("#FFA07A")+"------------- TOUR DE "+pseudoNoire+" -------------\n"+res)


                ech=initpiece2(ech,pieceBlanche,pieceNoire)
                if (tour%2 == 0):
                    affiche_plateau(ech,pieceBlanche, pieceNoire,last)
                else:
                    reverseAffiche_plateau(ech,pieceBlanche, pieceNoire,last)
                
                last=deplacementm(tour, ech, pieceBlanche, pieceNoire)
                os.system("cls")
                ech=initpiece2(ech,pieceBlanche,pieceNoire)
                if (tour%2 == 0):
                    affiche_plateau(ech,pieceBlanche, pieceNoire,last)
                else:
                    reverseAffiche_plateau(ech,pieceBlanche, pieceNoire,last)

                victoire=verifVictoire(pieceBlanche, pieceNoire)               
                tour += 1

        #affiche l'equipe gagnante
        if(victoire == -1):
            savePart(pieceBlanche,pieceNoire,tour)
        if(victoire == 1):
            print("\n"+fg(222)+str(pseudoNoire)+" remporte cette partie !"+res)
            eqBlanche=[pseudoBlanche, "0"]
            eqNoire=[pseudoNoire,"1"]
            score(eqBlanche,eqNoire)

            
        
        elif(victoire == 2):
            print("\n"+fg(222)+str(pseudoBlanche)+" remporte cette partie !"+res)
            eqBlanche=[pseudoBlanche, "1"]
            eqNoire=[pseudoNoire,"0"]
            score(eqBlanche,eqNoire)
            
        else:
            eqBlanche=[pseudoBlanche, "2"]
            eqNoire=[pseudoNoire,"2"]
            score(eqBlanche,eqNoire)
        att=-1
        while(att==-1):
            att=input(fg("#FFA07A")+"APPUYEZ SUR ENTRER POUR RETOURNER AU MENU PRINCIPAL"+res)
        
    elif (menu == 2):
        pieceBlanche = initCoordPieceB()
        pieceNoire = initCoordPieceN()
        os.system("cls")
        victoire = 0
        tour = 0
        test = True
        
        print(fg("#FFA07A")+"Quelle équipe voulez-vous jouer ?\n"+res)
        eqp=-1
        while(eqp != 1 and eqp != 0):
            eqp=int(input(fg("#00D7FA")+"0:"+res+fg("#FFA07A")+" Equipe Blanche\n"+res+fg("#00D7FA")+"1:" +res+fg("#FFA07A")+" Equipe Noire \n"+res+fg("#FF0000")+"-> "+res))
            if(eqp != 1 and eqp != 0):
                print(fg("#FF0000")+"Veuillez repondre 0 ou 1 !"+res)
            last=""
        if(eqp==1):
            pseudoBlanche="BOT"
            pseudoNoire=input(fg("#FFA07A")+"Equipe NOIRE | Entrez votre pseudo : "+res)
            
        else:
            pseudoBlanche=input(fg("#FFA07A")+"Equipe Blanche | Entrez votre pseudo : "+res)
            pseudoNoire="BOT"
        while(victoire == 0):
            if(tour > 0):
                #demande si ils veulent continuer la partie
                choix = 0
                while(choix != 1 and choix != 2 ):
                    print(fg("#00D7FA")+"1-"+res+fg("#FFA07A")+" CONTINUER LA PARTIE\n"+res+fg("#00D7FA")+"2-"+res+fg("#FFA07A")+" QUITTER LA PARTIE"+res)
                    choix = int(input())
                if( choix == 2):
                    victoire = -1
                    test = False
                

            os.system("cls")
            
            if(test==True):
                if (eqp == 0):
                    print(fg("#FFA07A")+"------------ TOUR DE L EQUIPE BLANCHE ------------\n"+res)
            
                
                if(eqp==0):
                    
                    ech=initpiece2(ech,pieceBlanche,pieceNoire)
                    affiche_plateau(ech,pieceBlanche, pieceNoire,last)
                    if(tour%2==0):
                        last=deplacementm(tour, ech, pieceBlanche, pieceNoire)
                    else:
                        last=deplacementBot(eqp,ech, pieceBlanche, pieceNoire)
                    os.system("cls")
                    ech=initpiece2(ech,pieceBlanche, pieceNoire)
                    affiche_plateau(ech,pieceBlanche, pieceNoire,last)
                    victoire=verifVictoire(pieceBlanche, pieceNoire)               
                    tour += 1

                else:
                    ech=initpiece2(ech,pieceBlanche,pieceNoire)
                    reverseAffiche_plateau(ech,pieceBlanche, pieceNoire,last)
                    if(tour%2==0):
                        last=deplacementBot(eqp,ech, pieceBlanche, pieceNoire)
                        
                    else:
                        last=deplacementm(tour, ech, pieceBlanche, pieceNoire)
                        
                    os.system("cls")
                    ech=initpiece2(ech,pieceBlanche, pieceNoire)
                    reverseAffiche_plateau(ech,pieceBlanche, pieceNoire,last)
                    victoire=verifVictoire(pieceBlanche, pieceNoire)               
                    tour += 1
                    

                                   
                    


        #affiche l'equipe gagnante
        if(victoire == 1):
            print(fg(222)+str(pseudoNoire)+" remporte cette partie !"+res)
            eqBlanche=[pseudoBlanche, "0"]
            eqNoire=[pseudoNoire,"1"]
            
        
        elif(victoire == 2):
            print(fg(222)+str(pseudoBlanche)+" remporte cette partie !"+res)
            eqBlanche=[pseudoBlanche, "1"]
            eqNoire=[pseudoNoire,"0"]
        else:
            eqBlanche=[pseudoBlanche, "0"]
            eqNoire=[pseudoNoire,"0"]
        score(eqBlanche,eqNoire)
        att=-1
        while(att==-1):
            att=input(fg("#FF0000")+"APPUYEZ SUR ENTRER POUR RETOURNER AU MENU PRINCIPAL"+res)
    elif(menu == 4):
        leave=-1
        while(leave == -1):

            os.system("cls")
            affiche_score()
            leave=input(fg("#FF0000")+"APPUYEZ SUR ENTRER POUR RETOURNER AU MENU PRINCIPAL : "+res)
    
    
    elif (menu == 5):
        start = 0





'''
1- affiche c est le tour de quelle equipe
2- place les pions
3- affiche le plateau
4-appel la fonction deplacement
5- tour+=1
6- 
'''