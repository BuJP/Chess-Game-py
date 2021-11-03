from pions import attr, actualiseReachN,actualiseReachB,recupPosB,recupPosN,fg,coordone
from affichage import affiche_plateau, affiche_plateau_reach,reverseAffiche_plateau_reach
import os
import random
'''
#permet de deplacer les pions sur le plateau 
def deplacement():



    tour = 0
    if tour % 2 == 0 :
      tabPiece = pieceBlanche
      reachEquipeJ = actualiseReachB()
      reachEquipeE = actualiseReachN()
    else:
      tabPiece = pieceNoire
      reachEquipeJ = actualiseReachN()
      reachEquipeE = actualiseReachB()

    #demande les coordoné du pion a deplacer
    test = False
    while(test == False):
      coordPion = input("Quel est les coordoné du pion que vous voulez deplacer ?")
      test = coordPion in coordone

    test = False
    while(test == False):
      coordPionFinal = input("ou voulez vous le placer ?")
      test = coordPionFinal in coordone

    #recherche du pion et modifie ses coordoné

    i=0
    while(i< len(tabPiece)):
      m = tabPiece[i]
      if(m["coord"]== coordPion):
        m["coord"]= coordPionFinal
        if (tour % 2 ==0):
          pieceBlanche[i] = m
        else:
          pieceNoire[i]= m
        
        indexCoord = coordone.index(coordPion)
        ech[indexCoord]="0"
        
        i= len(tabPiece)
      else:
        i+=1
'''
def deplacementm(tour, ech, pieceBlanche, pieceNoire):
  lvlupB=["a8","b8","c8","d8","e8","f8","g8","h8"]
  lvlupN=["a1","b1","c1","d1","e1","f1","g1","h1"]

  res = attr('reset')
  #a modifier
  

  actualiseReachB(pieceBlanche, ech, pieceNoire)
  actualiseReachN(pieceNoire, ech, pieceBlanche)

  if(tour%2==0):
    posEquipeJ = recupPosB(pieceBlanche)
    posEquipeE = recupPosN(pieceNoire)
    piece = pieceBlanche
  else:
    posEquipeJ = recupPosN(pieceNoire) 
    posEquipeE = recupPosB(pieceBlanche)
    piece = pieceNoire

  #verifie que le pion existe et peux se deplacer
 
  test = False
  while (test == False):
    initpos = ""
    if(initpos not in posEquipeJ):
      
      initpos = input(fg("#FFA07A")+"\nPiece à deplacer : "+res)
    
    if(initpos in posEquipeJ):
      #recupere son indice
      x=posEquipeJ.index(initpos)
      save = piece[x]
      if(save["reach"] == []):
        print(fg("#FF0000")+"Vous ne pouvez effectuer aucun déplacement avec cette pièce !\nchoisissez une autre pièce ! "+res)
        
      else:
        os.system("cls")
        if(tour%2==0):
          affiche_plateau_reach(ech, pieceBlanche, pieceNoire, save)
        else:
          reverseAffiche_plateau_reach(ech, pieceBlanche, pieceNoire, save)
        print(fg("#FFA07A")+"\ndeplacement possible : "+res,fg("#FFFF00")+" - ".join(save["reach"])+res)

        #demande si il veux changer de piece
        testChoix = False
        
        while(testChoix == False ):
          choix=input(fg("#FFA07A")+"Voulez-vous changez de piece ?"+res+fg("#FFFF00")+" (oui/non) : "+res)
          
          if(choix == "o" or choix== "oui"):
            testChoix = True
          
          elif(choix == "n" or choix == "non"):
            
            test = True
            testChoix = True
          else :
            print(fg("#FF0000")+"Veuillez repondre par oui ou non !"+res)

    else:
      print(fg("#FF0000")+"Aucune piece trouvé !\nveuillez entrer des coordonnés présents dans cette liste : "+res,fg("#FFFF00")+ " - ".join(posEquipeJ)+res )
      
  
  #Modification du dico + tab ech -------------------------------------------
  
  if(len(save["reach"])== 1):
    s = save["reach"]
    posFinal = s[0]

  else:
    os.system("cls")
    
    if(tour%2==0):
      affiche_plateau_reach(ech, pieceBlanche, pieceNoire, save)
    else:
      reverseAffiche_plateau_reach(ech, pieceBlanche, pieceNoire, save)
    test = False
    while(test==False):
      print(fg("#FFA07A")+"\ndeplacement possible : "+res,fg("#FFFF00")+" - ".join(save["reach"])+res)
      posFinal=input(fg("#FFA07A")+"Ou voulez-vous déplacer cette pièce ?"+res)

      if(posFinal not in save["reach"]):
        print(fg("#FF0000")+"impossible de déplacer cette pièce aux coordonne saisie : Entrez des coordonnés valides !"+res)
        
      
      else:
        test = True
        
  
  #remplace la case ou il est par un 0
  indexinit= coordone.index(initpos)
  ech[indexinit] = "0"
  #si il y a un pion ennemeie il supprime le pions 
  if (posFinal in posEquipeE):


    #recupere l indice du pion a supprimer
    x2=posEquipeE.index(posFinal)
    if(tour%2==0):
      del pieceNoire[x2]
      
    else:
      del pieceBlanche[x2]
    

  #deplace les coordoné dans le dico de piece
  #recupere l'indice du pion a modifier
  x3= posEquipeJ.index(initpos)
  if( tour%2==0):
    dico = pieceBlanche[x3]
    
    dico["coord"]= posFinal
    if(dico["type"]=="p" and dico["coord"] in lvlupB):
      evolution=""
      while(evolution!="c" and evolution!="d" and evolution!="t" and  evolution!="f" ):
        evolution=input("En quoi voulez vous faire evoluer votre pion ? (c / d / t / f)")
        if(evolution!="c" and evolution!="d" and evolution!="t" and evolution!="f"):
          print("veuillez repondre avec un des ces caractere: (c / d / t / f) ")
        dico["type"]=evolution
    pieceBlanche[x3]= dico
    
  else:
    dico = pieceNoire[x3]
    dico["coord"]= posFinal
    if(dico["type"]=="p" and dico["coord"] in lvlupN):
      evolution=""
      while(evolution!="c" and evolution!="d" and evolution!="t" and  evolution!="f" ):
        evolution=input("En quoi voulez vous faire evoluer votre pion ? (c / d / t / f)")
        if(evolution!="c" and evolution!="d" and evolution!="t" and evolution!="f"):
          print("veuillez repondre avec un des ces caractere: (c / d / t / f) ")
        dico["type"]=evolution
    pieceNoire[x3]= dico
  
  
  
  return dico["coord"]

def deplacementBot(eqp, ech, pieceBlanche, pieceNoire):
  
  #a modifier
  actualiseReachB(pieceBlanche, ech, pieceNoire)
  actualiseReachN(pieceNoire, ech, pieceBlanche)

  if(eqp==1):
    posEquipeJ = recupPosB(pieceBlanche)
    posEquipeE = recupPosN(pieceNoire)
    piece = pieceBlanche
  else:
    posEquipeJ = recupPosN(pieceNoire) 
    posEquipeE = recupPosB(pieceBlanche)
    piece = pieceNoire
  
  test=False
  while(test==False):
    pionalea=random.randint(0,len(piece)-1)
    x = piece[pionalea]
    
    if(len(x["reach"])>0):

      initpos=x["coord"]
      indexinit= coordone.index(initpos)
      ech[indexinit] = "0"
      maxi=len(x["reach"])-1
      reachAlea = random.randint(0,maxi)
      m=x["reach"]
      posFinal=m[reachAlea]
      
      
      if (posFinal in posEquipeE):
        #recupere l indice du pion a supprimer
        x2=posEquipeE.index(posFinal)
        if(eqp == 1):
          del pieceNoire[x2]
          
        else:
          del pieceBlanche[x2]
      
      x3= posEquipeJ.index(initpos)
      if( eqp ==1):

        dico = pieceBlanche[x3]
        dico["coord"]= posFinal
        pieceBlanche[x3]= dico
        
      else:
        dico = pieceNoire[x3]
        dico["coord"]= posFinal
        print(dico["coord"])
        pieceNoire[x3]= dico
      
      test=True
  return dico["coord"]


        





def verifVictoire(pieceBlanche, pieceNoire):
  x =pieceBlanche[len(pieceBlanche)-1]
  x2 =pieceNoire[len(pieceNoire)-1]
  if(x["type"]!= "r"):
    return 1

  elif(x2["type"]!= "r"):
    return 2
  else :
    return 0
"""
def reachRm(pieceJouant, pieceEnnemie, rois, reachEnnemie):
  #recupere les coordones des piece enemie
  coordEnemie = tabCoordonePieces(pieceEnnemie)
  #recupere les coordones de celui qui joue
  coordJouant = tabCoordonePieces(pieceJouant)
  #recupere le dictionnaire a modifier le 1
  savePiece = rois
  #recupere les coordone du pion
  coordonePiece = savePiece["coord"]
  
  reach=[]
  indice=coordone.index(coordonePiece)
  #remonte de une case en haut
  
  
  #si le pion se retouve sur la bordure de droite :

  if (coordone[indice] in bordureD):
    indice = indice - 8
    if( indice >= 0 and coordone[indice] in coordEnemie or ech[indice] == "0" ):
      if(coordone[indice] not in reachEnnemie):
        reach.append(coordone[indice])
      indice-=1
      if( indice >= 0 and coordone[indice] in coordEnemie or ech[indice] == "0"   ):
        if( coordone[indice] not in reachEnnemie):
          reach.append(coordone[indice])
    
    indice=coordone.index(coordonePiece)
    #descend de une case
    indice = indice + 8
    if( indice <= 63 and coordone[indice] in coordEnemie or ech[indice] == "0" ):
      if(coordone[indice] not in reachEnnemie):
        reach.append(coordone[indice])
      indice-=1
      if( indice <=63 and coordone[indice] in coordEnemie or ech[indice] == "0"   ):
        if( coordone[indice] not in reachEnnemie):
          reach.append(coordone[indice]) 

    indice=coordone.index(coordonePiece)
    #case de gauche
    indice-=1
    if( indice <= 63 and coordone[indice] in coordEnemie or ech[indice] == "0"  ):
      if(coordone[indice] not in reachEnnemie):
        reach.append(coordone[indice])

  #si le pion se retouve sur la bordure de gauche :
  elif(coordone[indice] in bordureG):
    indice = indice - 8
    if( indice >= 0 and coordone[indice] in coordEnemie or ech[indice] == "0"  ):
      if(coordone[indice] not in reachEnnemie):
        reach.append(coordone[indice])
      indice+=1
      if( indice >= 0 and coordone[indice] in coordEnemie or ech[indice] == "0"   ):
        if( coordone[indice] not in reachEnnemie):
          reach.append(coordone[indice])


    indice=coordone.index(coordonePiece)
    #descend de une case
    indice = indice + 8
    if( indice <= 63 and coordone[indice] in coordEnemie or ech[indice] == "0"  ):
      if(coordone[indice] not in reachEnnemie):
        reach.append(coordone[indice])
      indice+=1
      if(indice <=63 and coordone[indice] in coordEnemie or ech[indice] == "0"   ):
        if( coordone[indice] not in reachEnnemie):
          reach.append(coordone[indice]) 


    indice=coordone.index(coordonePiece)
    #case de droite
    indice+=1
    if(  indice <= 63 and coordone[indice] in coordEnemie or ech[indice] == "0"):
      if(coordone[indice] not in reachEnnemie):
        reach.append(coordone[indice])
  
  else:
    indice = indice - 8
    if( indice >= 0 and coordone[indice] in coordEnemie or ech[indice] == "0"  ):
      if(coordone[indice] not in reachEnnemie):
        reach.append(coordone[indice])
      indice+=1
      if(indice >= 0 and coordone[indice] in coordEnemie or ech[indice] == "0"   ):
        if( coordone[indice] not in reachEnnemie):
          reach.append(coordone[indice])
      indice-=2
      if(indice >= 0 and coordone[indice] in coordEnemie or ech[indice] == "0"  ):
        if( coordone[indice] not in reachEnnemie):
          reach.append(coordone[indice])
    

    indice=coordone.index(coordonePiece)
    indice = indice + 8
    print(indice)
    if(indice <= 63 and coordone[indice] in coordEnemie or ech[indice] == "0"  ):
      if(coordone[indice] not in reachEnnemie):
        reach.append(coordone[indice])
      indice+=1
      if(indice <=63 and coordone[indice] in coordEnemie or ech[indice] == "0"   ):
        if( coordone[indice] not in reachEnnemie):
          reach.append(coordone[indice])
      indice-=2
      if( indice <= 63 and coordone[indice] in coordEnemie or ech[indice] == "0" ):
        if( coordone[indice] not in reachEnnemie):
          reach.append(coordone[indice])


    indice=coordone.index(coordonePiece)
    #case de droite
    indice+=1
    if(indice <= 63 and coordone[indice] in coordEnemie or ech[indice] == "0" ):
      if(coordone[indice] not in reachEnnemie):
        reach.append(coordone[indice])

    #case de gauche
    indice-=2
    if(indice >= 63 and coordone[indice] in coordEnemie or ech[indice] == "0"  ):
      if(coordone[indice] not in reachEnnemie):
        reach.append(coordone[indice])

  print(reach)"""