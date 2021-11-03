from colored import fg, bg, attr
from plateaux import coordone, bordureD, bordureG, switchBordureD,switchBordureG, switch, bordure
#piece blanche
pieceBlanche=[ {"type":"p", "coord":"a2", "reach":[0], "couleur":fg("#FFFFFF") }, {"type":"p", "coord":"b2", "reach":[0], "couleur":fg("#FFFFFF") },{"type":"p", "coord":"c2", "reach":[0], "couleur":fg("#FFFFFF") },{"type":"p", "coord":"d2", "reach":[0], "couleur":fg("#FFFFFF") },{"type":"p", "coord":"e2", "reach":[0], "couleur":fg("#FFFFFF") },{"type":"p", "coord":"f2", "reach":[0], "couleur":fg("#FFFFFF") },{"type":"p", "coord":"g2", "reach":[0], "couleur":fg("#FFFFFF") },{"type":"p", "coord":"h2", "reach":[0], "couleur":fg("#FFFFFF") },
               {"type":"t", "coord":"a1", "reach":[0], "couleur":fg("#FFFFFF") }, {"type":"t", "coord":"h1", "reach":[0], "couleur":fg("#FFFFFF") },
               {"type":"f", "coord":"c1", "reach":[0], "couleur":fg("#FFFFFF") }, {"type":"f", "coord":"f1", "reach":[0], "couleur":fg("#FFFFFF") },
               {"type":"c", "coord":"b1", "reach":[0], "couleur":fg("#FFFFFF") }, {"type":"c", "coord":"g1", "reach":[0], "couleur":fg("#FFFFFF") },
               {"type":"d", "coord":"d1", "reach":[0], "couleur":fg("#FFFFFF") },
               {"type":"r", "coord":"e1", "reach":[0], "couleur":fg("#FFFFFF") }
    
    ]

#piece noir
pieceNoire=[ {"type":"p", "coord":"a7", "reach":[0], "couleur":fg("#000000") }, {"type":"p", "coord":"b7", "reach":[0], "couleur":fg("#000000") },{"type":"p", "coord":"c7", "reach":[0], "couleur":fg("#000000") },{"type":"p", "coord":"d7", "reach":[0], "couleur":fg("#000000") },{"type":"p", "coord":"e7", "reach":[0], "couleur":fg("#000000") },{"type":"p", "coord":"f7", "reach":[0], "couleur":fg("#000000") },{"type":"p", "coord":"g7", "reach":[0], "couleur":fg("#000000") },{"type":"p", "coord":"h7", "reach":[0], "couleur":fg("#000000") },
               {"type":"t", "coord":"a8", "reach":[0], "couleur":fg("#000000") }, {"type":"t", "coord":"h8", "reach":[0], "couleur":fg("#000000") },
               {"type":"f", "coord":"c8", "reach":[0], "couleur":fg("#000000") }, {"type":"f", "coord":"f8", "reach":[0], "couleur":fg("#000000") },
               {"type":"c", "coord":"b8", "reach":[0], "couleur":fg("#000000") }, {"type":"c", "coord":"g8", "reach":[0], "couleur":fg("#000000") },
               {"type":"d", "coord":"d8", "reach":[0], "couleur":fg("#000000") },
               {"type":"r", "coord":"e8", "reach":[0], "couleur":fg("#000000") }
    ]








def initCoordPieceB():
  global pieceBlanche
  posinitBlanc=[ {"type":"p", "coord":"a2", "reach":[0], "couleur":fg("#FFFFFF") }, {"type":"p", "coord":"b2", "reach":[0], "couleur":fg("#FFFFFF") },{"type":"p", "coord":"c2", "reach":[0], "couleur":fg("#FFFFFF") },{"type":"p", "coord":"d2", "reach":[0], "couleur":fg("#FFFFFF") },{"type":"p", "coord":"e2", "reach":[0], "couleur":fg("#FFFFFF") },{"type":"p", "coord":"f2", "reach":[0], "couleur":fg("#FFFFFF") },{"type":"p", "coord":"g2", "reach":[0], "couleur":fg("#FFFFFF") },{"type":"p", "coord":"h2", "reach":[0], "couleur":fg("#FFFFFF") },
               {"type":"t", "coord":"a1", "reach":[0], "couleur":fg("#FFFFFF") }, {"type":"t", "coord":"h1", "reach":[0], "couleur":fg("#FFFFFF") },
               {"type":"f", "coord":"c1", "reach":[0], "couleur":fg("#FFFFFF") }, {"type":"f", "coord":"f1", "reach":[0], "couleur":fg("#FFFFFF") },
               {"type":"c", "coord":"b1", "reach":[0], "couleur":fg("#FFFFFF") }, {"type":"c", "coord":"g1", "reach":[0], "couleur":fg("#FFFFFF") },
               {"type":"d", "coord":"d1", "reach":[0], "couleur":fg("#FFFFFF") },
               {"type":"r", "coord":"e1", "reach":[0], "couleur":fg("#FFFFFF") }
    
    ]
  return posinitBlanc


def initCoordPieceN():
  global pieceNoire
  posinitNoire=[ {"type":"p", "coord":"a7", "reach":[0], "couleur":fg("#000000") }, {"type":"p", "coord":"b7", "reach":[0], "couleur":fg("#000000") },{"type":"p", "coord":"c7", "reach":[0], "couleur":fg("#000000") },{"type":"p", "coord":"d7", "reach":[0], "couleur":fg("#000000") },{"type":"p", "coord":"e7", "reach":[0], "couleur":fg("#000000") },{"type":"p", "coord":"f7", "reach":[0], "couleur":fg("#000000") },{"type":"p", "coord":"g7", "reach":[0], "couleur":fg("#000000") },{"type":"p", "coord":"h7", "reach":[0], "couleur":fg("#000000") },
               {"type":"t", "coord":"a8", "reach":[0], "couleur":fg("#000000") }, {"type":"t", "coord":"h8", "reach":[0], "couleur":fg("#000000") },
               {"type":"f", "coord":"c8", "reach":[0], "couleur":fg("#000000") }, {"type":"f", "coord":"f8", "reach":[0], "couleur":fg("#000000") },
               {"type":"c", "coord":"b8", "reach":[0], "couleur":fg("#000000") }, {"type":"c", "coord":"g8", "reach":[0], "couleur":fg("#000000") },
               {"type":"d", "coord":"d8", "reach":[0], "couleur":fg("#000000") },
               {"type":"r", "coord":"e8", "reach":[0], "couleur":fg("#000000") }
    ]
  return posinitNoire
  

  



#Place les pieces dans le tableau a leur coordoné
def initpiece2(ech, pieceBlanche,pieceNoire):
    
    i=0

    while(i<len(pieceBlanche)):
        x = pieceBlanche[i]
        j=0
        savecoord= ""
        while(j<len(coordone)):
          savecoord =  coordone[j]

          if (savecoord == x["coord"]):
            ech[j]=x["type"]
            j=len(coordone)
          else:
            j+=1
        

        i=i+1

    i=0
    while(i<len(pieceNoire)):
        x = pieceNoire[i]
        j=0
        savecoord= ""
        while(j<len(coordone)):
          savecoord =  coordone[j]

          if (savecoord == x["coord"]):
            ech[j]=x["type"]
            j=len(coordone)
          else:
            j+=1
        

        i=i+1
    
    return ech

'''
def initpiece2():
    res = attr('reset')
    i=0
    while(i<len(pieceBlanche)):
        x = pieceBlanche[i]
        j=0
        savecoord= ""
        while(j<len(coordone)):
          savecoord =  coordone[j]

          if (savecoord == x["coord"]):
            ech[j]= x["couleur"]+x["type"].rjust(3)+res
            j=len(coordone)
          else:
            j+=1
        

        i=i+1

    i=0
    while(i<len(pieceNoire)):
        x = pieceNoire[i]
        j=0
        savecoord= ""
        while(j<len(coordone)):
          savecoord =  coordone[j]

          if (savecoord == x["coord"]):
            ech[j]= x["couleur"]+x["type"].rjust(3)+res
            j=len(coordone)
          else:
            j+=1
        

        i=i+1'''

def tabCoordonePieces(dico):
  i=0
  tab = []
  while(i<len(dico)):
    x = dico[i]
    tab.append(x["coord"])
    i+=1
  return tab


"""MODIFIER LA FONCTION REACHP POUR FAIRE EN SORTE QUE AU PREMIER TOUR ILS PEUT AVANCER DE DEUX CASE AU LIEU D UNE"""
def reachP (couleur,pieceJouant, pieceEnnemie, pion, ech,bordureD, bordureG):
  
  #recupere les coordones des piece enemie
  x=tabCoordonePieces(pieceEnnemie)
  #recupere le dictionnaire
  savePiece = pion
  #recupere les coordone du pion
  coordonePiece = savePiece["coord"]
  #trouve son indice sur le plateau (son numero de case)
  indice=coordone.index(coordonePiece)
  #prend l'indice du haut
  indice=indice-8
  reach = []
  i=0

  doubleN=["a7","b7","c7","d7","e7","f7","g7","h7"]
  doubleB=["a2","b2","c2","d2","e2","f2","g2","h2"]
  
  while (i<1 and indice >= 0 and indice <= 63):
    
    
    

    #verifie si sur l'echiquier l'emplacement est vide
    if (ech[indice] == "0"):
      #si l'echiquier est vide il rajoute les coordones au tableau
      reach.append(coordone[indice])
      if(couleur == "b" and coordonePiece in doubleB):
        indice = indice - 8
        if (ech[indice] == "0"):
          #si l'echiquier est vide il rajoute les coordones au tableau
          reach.append(coordone[indice])
      
      if(couleur == "n" and coordonePiece in doubleN):
        indice = indice - 8
        if (ech[indice] == "0"):
          #si l'echiquier est vide il rajoute les coordones au tableau
          reach.append(coordone[indice])
      

      i+=1
      
    else:
      i=2

    
  #verifie si le pion peut manger une piece
  
  indice=coordone.index(coordonePiece)
  

  
  if(coordone[indice] in bordureD):
    indice-= 9
    if (coordone[indice] in x):
        reach.append(coordone[indice])
  elif(coordone[indice]in bordureG):
    indice-= 7
    if (coordone[indice] in x):
        reach.append(coordone[indice])

  else:  
    indice-= 9
    i=0
    
    while(i<2 and indice >= 0 and indice <= 63 ):
      i2=0
      while (i2 < 2 and indice >= 0 and indice <= 63):
        if (coordone[indice] in x):
          reach.append(coordone[indice])
        indice+=2
        i2+=1
      i+=1
      indice+=16

          
  #remplace le tableau dans le dictionnaire de la piece
  return reach




def reachT(pieceJouant, pieceEnnemie, tour, ech,bordureD, bordureG):
  """De manière générale la tour se déplace horizontalement ou verticalement d'autant de cases qu'elle souhaite si elle ne rencontre pas d'obstacle.
  Si elle rencontre un obstacle de couleur adverse, la tour n'a pas le droit de sauter par-dessus, par contre elle est en droit de prendre la pièce en s'arrêtant sur la case où la pièce adverse se trouvait.
  Si elle rencontre un obstacle de même couleur qu'elle, elle ne peut pas sauter par-dessus et est dans l'obligation de s'arrêter au plus loin dans la case adjacente."""

  #recupere les coordones des piece enemie
  coordEnemie = tabCoordonePieces(pieceEnnemie)
  #recupere les coordones de celui qui joue
  coordJouant = tabCoordonePieces(pieceJouant)
  #recupere le dictionnaire a modifier le 1
  savePiece = tour
  #recupere les coordone du pion
  coordonePiece = savePiece["coord"]
  
  #trouve son indice sur le plateau (son numero de case)
  indice=coordone.index(coordonePiece)
  
  indice+=8
  reach=[]

  test= True
  #verifie les coordones en dessous de la tour
  while (test == True and indice <= 63):
    
    
    if(coordone[indice] in coordEnemie):
      test = False
      reach.append(coordone[indice])

    if(coordone[indice] in coordJouant):
      test = False
    if(ech[indice]== "0"):
      reach.append(coordone[indice])
      indice = indice + 8



  #verifie les cordone du haut:
  indice=coordone.index(coordonePiece)
  indice = indice - 8
  test= True
  
  while (test == True and indice >=0):
    
    
    if(coordone[indice] in coordEnemie):
      test= False
      
      reach.append(coordone[indice])
    if(coordone[indice] in coordJouant):
      test = False
    if(ech[indice]== "0"):
      reach.append(coordone[indice])
      indice = indice - 8
  


    #verifie les cordone a droite:
  test= True
  indice=coordone.index(coordonePiece)
  if (coordone[indice] in bordureD):
      test=False
 

  indice = indice + 1
  
  while (test == True and indice <=63):
    if (coordone[indice] in bordure):
      test=False

    if(coordone[indice] in coordEnemie):
      test= False
      
      reach.append(coordone[indice])
    if(coordone[indice] in coordJouant):
      test = False
    if(ech[indice]== "0"):
      reach.append(coordone[indice])
      indice = indice +1
    
  #verifie les cordone a gauche:
  test= True
  indice=coordone.index(coordonePiece)

  if (coordone[indice] in bordureG):
      test=False
  indice = indice - 1
  
  
  while (test == True and indice >=0):
    if (coordone[indice] in bordureG):
      test=False
      
    if(coordone[indice] in coordEnemie):
      test= False
      
      reach.append(coordone[indice])
    if(coordone[indice] in coordJouant):
      test = False
    if(ech[indice]== "0"):
      reach.append(coordone[indice])
      indice = indice -1
    

  
  return reach

def reachF(pieceJouant, pieceEnnemie, fou, ech,bordureD, bordureG):
  #recupere les coordones des piece enemie
  coordEnemie = tabCoordonePieces(pieceEnnemie)
  #recupere les coordones de celui qui joue
  coordJouant = tabCoordonePieces(pieceJouant)
  #recupere le dictionnaire a modifier le 1
  savePiece = fou
  #recupere les coordone du pion
  coordonePiece = savePiece["coord"]
  
  reach=[]

  #verifie les cordone de la diagonale en haut a droite:
  indice=coordone.index(coordonePiece)
  
  if(coordone[indice] not in bordureD):
    test= True
    indice = indice - 7
  else:
    test=False

  while (test == True and indice >=0 and indice <= 63):
    if (coordone[indice] in bordureG):
      test=False
      
    if(coordone[indice] in coordEnemie):
      test= False
      
      reach.append(coordone[indice])
    if(coordone[indice] in coordJouant):
      test = False
    if(ech[indice]== "0"):
      reach.append(coordone[indice])
      indice = indice -7

   #verifie les cordone de la diagonale en haut a gauche:
  indice=coordone.index(coordonePiece)
 
  
  
  if(coordone[indice] not in bordureG):
    test= True
    indice = indice - 9
  else:
    test=False

  while (test == True and indice >=0 and indice <= 63):
    if (coordone[indice] in bordureG):
      test=False
      
    if(coordone[indice] in coordEnemie):
      test= False
      
      reach.append(coordone[indice])
    if(coordone[indice] in coordJouant):
      test = False
    if(ech[indice]== "0"):
      reach.append(coordone[indice])
      indice = indice -9
  
    #verifie les cordone de la diagonale en bas a droite:
  indice=coordone.index(coordonePiece)

  if(coordone[indice] not in bordureD):
    test= True
    indice = indice +9
  else:
    test=False

  while (test == True and indice >=0 and indice <= 63):
    if (coordone[indice] in bordureD):
      test=False
      
    if(coordone[indice] in coordEnemie):
      test= False
      
      reach.append(coordone[indice])
    if(coordone[indice] in coordJouant):
      test = False
    if(ech[indice]== "0"):
      reach.append(coordone[indice])
      indice = indice +9
  
    #verifie les cordone de la diagonale en bas a gauche:
  indice=coordone.index(coordonePiece)
  
  if(coordone[indice] not in bordureG):
    test= True
    indice = indice + 7
  else:
    test=False

  while (test == True and indice >=0 and indice <= 63):
    if (coordone[indice] in bordureD):
      test=False
      
    if(coordone[indice] in coordEnemie):
      test= False
      
      reach.append(coordone[indice])
    if(coordone[indice] in coordJouant):
      test = False
    if(ech[indice]== "0"):
      reach.append(coordone[indice])
      indice = indice + 7
   
  
  return reach

def reachD(pieceJouant, pieceEnnemie, dame, ech, bordureD, bordureG):
  #la dame possede les deplacement du fou et de la tour
  a = reachF(pieceJouant, pieceEnnemie, dame, ech,bordureD, bordureG)
  a= a + reachT(pieceJouant, pieceEnnemie, dame, ech,bordureD, bordureG)
  
  return a


def reachRm(pieceJouant, pieceEnnemie, rois, ech, bordureD, bordureG):
  #recupere les coordones des piece enemie
  coordEnemie = tabCoordonePieces(pieceEnnemie)
  #recupere les coordones de celui qui joue
  #---------------
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
    if( indice >= 0):
      if(coordone[indice] in coordEnemie or ech[indice] == "0" ):
        reach.append(coordone[indice])
      indice-=1
      if( indice >= 0    ):
        if(   coordone[indice] in coordEnemie or ech[indice] == "0"):
          reach.append(coordone[indice])
    
    indice=coordone.index(coordonePiece)
    #descend de une case
    indice = indice + 8
    if( indice <= 63  ):
      if(coordone[indice] in coordEnemie or ech[indice] == "0"):
        reach.append(coordone[indice])
      indice-=1
      if( indice <=63    ):
        if(  coordone[indice] in coordEnemie or ech[indice] == "0"):
          reach.append(coordone[indice]) 

    indice=coordone.index(coordonePiece)
    #case de gauche
    indice-=1
    if( indice <= 63   ):
      if( coordone[indice] in coordEnemie or ech[indice] == "0"):
        reach.append(coordone[indice])

  #si le pion se retouve sur la bordure de gauche :
  elif(coordone[indice] in bordureG):
    indice = indice - 8
    if( indice >= 0   ):
      if( coordone[indice] in coordEnemie or ech[indice] == "0"):
        reach.append(coordone[indice])
      indice+=1
      if( indice >= 0    ):
        if( coordone[indice] in coordEnemie or ech[indice] == "0"):
          reach.append(coordone[indice])


    indice=coordone.index(coordonePiece)
    #descend de une case
    indice = indice + 8
    if( indice <= 63   ):
      if( coordone[indice] in coordEnemie or ech[indice] == "0"):
        reach.append(coordone[indice])
      indice+=1
      if(indice <=63    ):
        if(  coordone[indice] in coordEnemie or ech[indice] == "0"):
          reach.append(coordone[indice]) 


    indice=coordone.index(coordonePiece)
    #case de droite
    indice+=1
    if(  indice <= 63):
      if(coordone[indice] in coordEnemie or ech[indice] == "0"):
        reach.append(coordone[indice])
  
  else:
    indice = indice - 8
    if( indice >= 0   ):
      if( coordone[indice] in coordEnemie or ech[indice] == "0"):
        reach.append(coordone[indice])
      indice+=1
      if(indice >= 0    ):
        if(  coordone[indice] in coordEnemie or ech[indice] == "0"):
          reach.append(coordone[indice])
      indice-=2
      if(indice >= 0  ):
        if(coordone[indice] in coordEnemie or ech[indice] == "0"):
          reach.append(coordone[indice])
    

    indice=coordone.index(coordonePiece)
    indice = indice + 8
    
    if(indice <= 63   ):
      if(coordone[indice] in coordEnemie or ech[indice] == "0"):
          reach.append(coordone[indice])
      indice+=1
      if(indice <=63    ):
        if( coordone[indice] in coordEnemie or ech[indice] == "0"):
          reach.append(coordone[indice])
      indice-=2
      if( indice <= 63  ):
        if( coordone[indice] in coordEnemie or ech[indice] == "0"):
          reach.append(coordone[indice])


    indice=coordone.index(coordonePiece)
    #case de droite
    indice+=1
    if(indice <= 63  ):
      if( coordone[indice] in coordEnemie or ech[indice] == "0"):
        reach.append(coordone[indice])

    #case de gauche
    indice-=2
    if(indice <= 63   ):
      if( coordone[indice] in coordEnemie or ech[indice] == "0") :
        reach.append(coordone[indice])

  return reach

'''
def reachR(pieceJouant, pieceEnnemie, rois, reachEnnemie):
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
  indice = indice - 7
  i = 0
  if (coordone[indice] in bordureG):
      indice=coordone.index(coordonePiece)
      indice-=8
      i=1

  while (i<3 and indice >=0 and indice <= 63):
    
    if (coordone[indice] in bordureG ):
      i=3
    if(coordone[indice] in coordEnemie and coordone[indice] not in reachEnnemie):
      reach.append(coordone[indice])
      i+=1
      
    if(coordone[indice] in coordJouant):
      i+=1
    if(ech[indice] == "0" and coordone[indice] not in reachEnnemie):
      reach.append(coordone[indice])
      i+=1
      
    indice-=1
    
  # verifie la ligne du bas


  indice=coordone.index(coordonePiece)
  indice = indice + 7
  i = 0
  
  while (i<3 and indice >=0 and indice <= 63):
    if (coordone[indice] in bordureD):
      i=3
    if(coordone[indice] in coordEnemie and coordone[indice] not in reachEnnemie):
      reach.append(coordone[indice])
      i+=1
      
    if(coordone[indice] in coordJouant):
      i+=1
    if(ech[indice] == "0" and coordone[indice] not in reachEnnemie):
      reach.append(coordone[indice])
      
    indice+=1
 #verifie les cote

  indice=coordone.index(coordonePiece)

  if (coordone[indice] not in bordureD):
    indice+=1
    if(coordone[indice] in coordEnemie and coordone[indice] not in reachEnnemie):
      reach.append(coordone[indice])
      indice-=1
    
    if(ech[indice] == "0"):
      reach.append(coordone[indice])
      indice-=1
  
  if (coordone[indice] not in bordureG):
      indice-=1  
      if(coordone[indice-1] in coordEnemie and coordone[indice] not in reachEnnemie):
        reach.append(coordone[indice])
          
    
      if(ech[indice] == "0" and coordone[indice] not in reachEnnemie):
        reach.append(coordone[indice])
    #regler le faite que a h4 il y a un bug pour la reach
  
  return reach
'''

def reachC(pieceJouant, pieceEnnemie, cavalier,bordureG, bordureD, ech):


   #recupere les coordones des piece enemie
  coordEnemie = tabCoordonePieces(pieceEnnemie)
  #recupere les coordones de celui qui joue
  #----------------
  #recupere le dictionnaire a modifier le 1
  savePiece = cavalier
  #recupere les coordone du pion
  coordonePiece = savePiece["coord"]
  
  reach=[]

  indice=coordone.index(coordonePiece)
  
  #------------DEUX CASE DU HAUT :

  if (coordone[indice] in bordureG):
    
    #remonte de deux case en haut
    indice-= 16
    #prend la case a droite
    indice+=1
    if(indice>=0 and ech[indice]=="0" or coordone[indice] in coordEnemie):
      reach.append(coordone[indice])
  
  elif(coordone[indice]in bordureD):
    indice-= 16
    #prend la case a gauche
    indice-=1
    if(indice>=0 and ech[indice]=="0" or coordone[indice] in coordEnemie):
      reach.append(coordone[indice])
  
  else:
    indice-= 16
    #prend la case a droite
    indice+=1
    if(indice>=0 and ech[indice]=="0" or coordone[indice] in coordEnemie):
      reach.append(coordone[indice])
    indice-=2
    if(indice>=0 and ech[indice]=="0" or coordone[indice] in coordEnemie):
      reach.append(coordone[indice])
  

   #------------DEUX CASE DU BAS :
  indice=coordone.index(coordonePiece)

  if (coordone[indice] in bordureG):
    #remonte de deux case en haut
    indice+= 16
    #prend la case a droite
    indice+=1
    if(indice<=63 and indice >=0 ):
      if(ech[indice]=="0" or coordone[indice] in coordEnemie):
        reach.append(coordone[indice])      
      
  
  elif(coordone[indice]in bordureD):
    indice+= 16
    #prend la case a gauche
    indice-=1
    if(indice<=63 and indice >=0):
      if(ech[indice]=="0" or coordone[indice] in coordEnemie):
        reach.append(coordone[indice])
  
  else:
    indice+= 16
    #prend la case a droite
    indice+=1
    
    if(indice<=63 and ech[indice]=="0" ):
      #CAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
      if (ech[indice]=="0" or coordone[indice] in coordEnemie):
        reach.append(coordone[indice])
    indice-=2
    if(indice<=63 and indice >=0):
      if (ech[indice]=="0" or coordone[indice] in coordEnemie):
        reach.append(coordone[indice])


  #DEUX CASE DE GAUCHE/

  indice=coordone.index(coordonePiece)
  if (coordone[indice] not in bordureD and indice <=63 ):
    indice+=1
    if (coordone[indice] not in bordureD and indice <=63 ):
      indice+=1
      indice+=8
      if (indice<=63 and indice >=0):
        if (ech[indice]=="0" or coordone[indice] in coordEnemie):
          reach.append(coordone[indice])
      indice-=16
      if (indice>=0 and indice <=63):
        if (ech[indice]=="0" or coordone[indice] in coordEnemie):
          reach.append(coordone[indice])
  

  #DEUX CASE DE droite:
  
  indice=coordone.index(coordonePiece)
  if (coordone[indice] not in bordureG and indice <=63 ):
    indice-=1
    if (coordone[indice] not in bordureG and indice <=63 ):
      
      indice-=1
      indice-=8

      if (indice<=63 and indice >=0):
        if (ech[indice]=="0" or coordone[indice] in coordEnemie):
          reach.append(coordone[indice])
      indice+=16
      if (indice>=0 and indice <=63):
        if (ech[indice]=="0" or coordone[indice] in coordEnemie):
          reach.append(coordone[indice])


  return reach


'''
1-  FAIRE UNE FONCTION QUI ACTUALISE
    LE TABLEAU REACH DES DEUX EQUIPE 
    ET CREE DEUX AUTRE TABLEAU AVEC
    TOUT LES DEPLACEMENT POSSIBLE DES EQUIPES
2-  QUI SERVIRA POUR UNE FONCTION
    ECHECS PERMETTANT DE VERIFIER
    LA OU LE ROIS PEUT SE DEPLACER
    ET SAVOIR SI IL EST EN ECHEC ET MAT
    '''

#permet d actualiser la reach de toute les piece de l equipe blanche sauf le rois
def actualiseReachB(pieceBlanche, ech, pieceNoire):
  reachEquipeBlanche = []
  #equipe blanche :
  i=0

  while(i<len(pieceBlanche)):
    #prend le dico a l indice i
    x= pieceBlanche[i]
    
    #appel la fonction coordone pour savoir ou le pion peut aller
    if (x["type"]== "p"):
      
      x["reach"]=  reachP("b",pieceBlanche, pieceNoire, x, ech,bordureD, bordureG)
      pieceBlanche[i]= x
    
    #Meme chose pour la tour
    elif (x["type"]== "t"):
      
      x["reach"]=  reachT(pieceBlanche, pieceNoire, x, ech,bordureD, bordureG)
      pieceBlanche[i]= x

    #Meme chose pour le fou
    elif (x["type"]== "f"):
      
      x["reach"]=  reachF(pieceBlanche, pieceNoire, x, ech,bordureD, bordureG)
      pieceBlanche[i]= x

    #Meme chose pour la dame
    elif (x["type"]== "d"):
      
      x["reach"]=  reachD(pieceBlanche, pieceNoire, x, ech, bordureD, bordureG)
      pieceBlanche[i]= x
    #Meme chose pour la rois
    elif (x["type"]== "r"):
      x["reach"]=  reachRm(pieceBlanche, pieceNoire, x, ech,bordureD, bordureG)
      pieceBlanche[i]= x


    #meme chose pour le cavalier
    elif (x["type"]== "c"):
      
      x["reach"]=  reachC(pieceBlanche, pieceNoire, x, bordureG, bordureD, ech)
      pieceBlanche[i]= x

    save = x["reach"]
    reachEquipeBlanche = reachEquipeBlanche + save
    
    i+=1
  return reachEquipeBlanche
  
#permet d actualiser la reach de toute les piece de l equipe noire sauf le rois
def actualiseReachN(pieceNoire, ech,pieceBlanche):
  switch(ech)
  

  reachEquipeNoire = []
  #equipe blanche :
  i=0
 
  while(i<len(pieceNoire)):
    #prend le dico a l indice i
    x= pieceNoire[i]
    
    #appel la fonction coordone pour savoir ou le pion peut aller
    if (x["type"]== "p"):
      
      x["reach"]=  reachP("n", pieceNoire, pieceBlanche, x, ech, switchBordureD, switchBordureG)
      pieceNoire[i]= x
    
    #Meme chose pour la tour
    elif (x["type"]== "t"):
      
      x["reach"]=  reachT( pieceNoire, pieceBlanche, x, ech, switchBordureD, switchBordureG)
      pieceNoire[i]= x

    #Meme chose pour le fou
    elif (x["type"]== "f"):
      
      x["reach"]=  reachF( pieceNoire, pieceBlanche, x, ech, switchBordureD, switchBordureG)
      pieceNoire[i]= x

    #Meme chose pour la dame
    elif (x["type"]== "d"):
      
      x["reach"]=  reachD( pieceNoire, pieceBlanche, x, ech, switchBordureD, switchBordureG)
      pieceNoire[i]= x
    #Meme chose pour la rois
    elif (x["type"]== "r"):
      
      x["reach"]=  reachRm( pieceNoire, pieceBlanche, x, ech,switchBordureD, switchBordureG)
      pieceNoire[i]= x

    #meme chose pour le cavalier
    elif (x["type"]== "c"):
      
      x["reach"]=  reachC( pieceNoire, pieceBlanche, x ,switchBordureG, switchBordureD, ech)
      pieceNoire[i]= x

    save = x["reach"]
    reachEquipeNoire = reachEquipeNoire + save
 
    i+=1

  switch(ech)
  return reachEquipeNoire


def recupPosB(pieceBlanche):

  i=0
  pos=[]
  while(i<len(pieceBlanche)):
      x= pieceBlanche[i]
      pos.append(x["coord"])
      i+=1
  return pos

def recupPosN(pieceNoire):

  i=0
  pos=[]
  while(i<len(pieceNoire)):
      x= pieceNoire[i]
      pos.append(x["coord"])
      i+=1
  return pos




