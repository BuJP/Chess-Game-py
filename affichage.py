

from coup import recupPosB,recupPosN, coordone
from plateaux import switch
from colored import fg, bg, attr


def affiche_plateau(ech, pieceBlanche, pieceNoire, last):
  
  ligne=""
  res = attr('reset')
  i=0
  i3=0
  a=""
  blanc=recupPosB(pieceBlanche)
  noire=recupPosN(pieceNoire)
  ligne=" ".ljust(4) +fg("#00D7FA")+"|"+res


    # affichage des lettre
  while(i<8):
    ligne=ligne+fg("#FF00C2")+chr(97+i).rjust(2)+res+fg("#00D7FA")+"|".rjust(3)+res
    i+=1
  print (ligne)
  i=0

  while(i<8):
    
    ligne=fg("#FF00C2") + chr(56-i).ljust(4) +res+fg("#00D7FA")+"|"+res
    i2=0
    print(fg("#00D7FA")+"--------------------------------------------------"+res)
    while(i2<8):
      if(ech[i3]=="p"):
        a="♟"
      elif(ech[i3]=="f"):
        a="♗"
      elif(ech[i3]=="t"):
        a="♖"
      elif(ech[i3]=="c"):
        a="♘"
      elif(ech[i3]=="r"):
        a="♔"
      elif(ech[i3]=="d"):
        a="♕"
      else:
        a=" "
      if(coordone[i3] in blanc):
        
        if(coordone[i3]==last):
          ligne=ligne+bg("#008000")+fg("#FFFFFF")+a.rjust(2).ljust(4)+res+res+fg("#00D7FA")+"|"+res
        else:
          ligne=ligne+fg("#FFFFFF")+a.rjust(2)+res+fg("#00D7FA")+"|".rjust(3)+res
          
      elif(coordone[i3] in noire):
         if(coordone[i3]==last):
           ligne=ligne+bg("#008000")+fg("#808080")+a.rjust(2).ljust(4)+res+fg("#00D7FA")+"|"+res
         else:
           ligne=ligne+fg("#808080")+a.rjust(2)+fg("#00D7FA")+"|".rjust(3)+res

        
    
      else:
        ligne=ligne+a.rjust(2)+fg("#00D7FA")+"|".rjust(3)+res
      i3+=1
      i2+=1

    ligne=ligne+fg("#FF00C2") + chr(56-i).rjust(4)
    print (ligne)
    i+=1

  ligne=" ".ljust(4) +fg("#00D7FA")+"|"+res
  i=0
  # affichage des lettre
  print(fg("#00D7FA")+"--------------------------------------------------"+res)
  while(i<8):
    ligne=ligne+fg("#FF00C2")+chr(97+i).rjust(2)+res+fg("#00D7FA")+"|".rjust(3)+res
    i+=1
  print (ligne)

def reverseAffiche_plateau(ech, pieceBlanche, pieceNoire, last):
  
  switch(ech)

  
  ligne=""
  res = attr('reset')
  i=0
  i3=0
  a=""
  blanc=recupPosB(pieceBlanche)
  noire=recupPosN(pieceNoire)
  ligne=" ".ljust(4) +fg("#00D7FA")+"|"+res


    # affichage des lettre
  while(i<8):
    ligne=ligne+fg("#FF00C2")+chr(104-i).rjust(2)+res+fg("#00D7FA")+"|".rjust(3)+res
    i+=1
  print (ligne)
  i=0

  while(i<8):
    
    ligne=fg("#FF00C2") + chr(49+i).ljust(4) +res+fg("#00D7FA")+"|"+res
    i2=0
    print(fg("#00D7FA")+"--------------------------------------------------"+res)
    while(i2<8):
      if(ech[i3]=="p"):
        a="♟"
      elif(ech[i3]=="f"):
        a="♗"
      elif(ech[i3]=="t"):
        a="♖"
      elif(ech[i3]=="c"):
        a="♘"
      elif(ech[i3]=="r"):
        a="♔"
      elif(ech[i3]=="d"):
        a="♕"
      else:
        a=" "
      if(coordone[i3] in blanc):
        
        if(coordone[i3]==last):
          ligne=ligne+bg("#008000")+fg("#FFFFFF")+a.rjust(2).ljust(4)+res+res+fg("#00D7FA")+"|"+res
        else:
          ligne=ligne+fg("#FFFFFF")+a.rjust(2)+res+fg("#00D7FA")+"|".rjust(3)+res
          
      elif(coordone[i3] in noire):
         if(coordone[i3]==last):
           ligne=ligne+bg("#008000")+fg("#808080")+a.rjust(2).ljust(4)+res+fg("#00D7FA")+"|"+res
         else:
           ligne=ligne+fg("#808080")+a.rjust(2)+fg("#00D7FA")+"|".rjust(3)+res

        
    
      else:
        ligne=ligne+a.rjust(2)+fg("#00D7FA")+"|".rjust(3)+res
      i3+=1
      i2+=1

    ligne=ligne+fg("#FF00C2") + chr(49+i).rjust(4)
    print (ligne)
    i+=1

  ligne=" ".ljust(4) +fg("#00D7FA")+"|"+res
  i=0
  # affichage des lettre
  print(fg("#00D7FA")+"--------------------------------------------------"+res)
  while(i<8):
    ligne=ligne+fg("#FF00C2")+chr(104-i).rjust(2)+res+fg("#00D7FA")+"|".rjust(3)+res
    i+=1
  print (ligne)
  switch(ech)

def affiche_plateau_reach(echvrai, pieceBlanche, pieceNoire, pions):
  x=[]
  ech=echvrai.copy()
  x=pions["reach"]


  
  ligne=""
  res = attr('reset')
  i=0
  i3=0
  a=""
  blanc=recupPosB(pieceBlanche)
  noire=recupPosN(pieceNoire)
  ligne=" ".ljust(4) +fg("#00D7FA")+"|"+res


    # affichage des lettre
  while(i<8):
    ligne=ligne+fg("#FF00C2")+chr(97+i).rjust(2)+res+fg("#00D7FA")+"|".rjust(3)+res
    i+=1
  print (ligne)
  i=0

  while(i<8):
    
    ligne=fg("#FF00C2") + chr(56-i).ljust(4) +res+fg("#00D7FA")+"|"+res
    i2=0
    print(fg("#00D7FA")+"--------------------------------------------------"+res)
    while(i2<8):
      if(ech[i3]=="p"):
        a="♟"
      elif(ech[i3]=="f"):
        a="♗"
      elif(ech[i3]=="t"):
        a="♖"
      elif(ech[i3]=="c"):
        a="♘"
      elif(ech[i3]=="r"):
        a="♔"
      elif(ech[i3]=="d"):
        a="♕"
      else:
        a=" "
      
      
      if(coordone[i3] in blanc):
        if(coordone[i3]in x):
          ligne=ligne+bg("#FF0000")+fg("#FFFFFF")+a.rjust(2).ljust(4)+res+res+fg("#00D7FA")+"|"+res
        else:
          ligne=ligne+fg("#FFFFFF")+a.rjust(2)+res+fg("#00D7FA")+"|".rjust(3)+res
        
      elif(coordone[i3] in noire):
        if(coordone[i3]in x):
          ligne=ligne+bg("#FF0000")+fg("#808080")+a.rjust(2).ljust(4)+res+fg("#00D7FA")+"|"+res
        
        else:
          ligne=ligne+fg("#808080")+a.rjust(2)+fg("#00D7FA")+"|".rjust(3)+res
        
    
      else:
        if(coordone[i3]in x):
          ligne=ligne+bg("#FF0000")+a.rjust(2).ljust(4)+res+fg("#00D7FA")+"|"+res
        else:
          ligne=ligne+a.rjust(2)+fg("#00D7FA")+"|".rjust(3)+res
        
      i3+=1
      i2+=1

    ligne=ligne+fg("#FF00C2") + chr(56-i).rjust(4)
    print (ligne)
    i+=1

  ligne=" ".ljust(4) +fg("#00D7FA")+"|"+res
  i=0
  # affichage des lettre
  print(fg("#00D7FA")+"--------------------------------------------------"+res)
  while(i<8):
    ligne=ligne+fg("#FF00C2")+chr(97+i).rjust(2)+res+fg("#00D7FA")+"|".rjust(3)+res
    i+=1
  print (ligne)


def reverseAffiche_plateau_reach(echvrai, pieceBlanche, pieceNoire, pions):
 
  
  
  x=[]
  ech=echvrai.copy()
  switch(ech)
  x=pions["reach"]


  
  ligne=""
  res = attr('reset')
  i=0
  i3=0
  a=""
  blanc=recupPosB(pieceBlanche)
  noire=recupPosN(pieceNoire)
  ligne=" ".ljust(4) +fg("#00D7FA")+"|"+res


    # affichage des lettre
  while(i<8):
    ligne=ligne+fg("#FF00C2")+chr(104-i).rjust(2)+res+fg("#00D7FA")+"|".rjust(3)+res
    i+=1
  print (ligne)
  i=0

  while(i<8):
    
    ligne=fg("#FF00C2") + chr(49+i).ljust(4) +res+fg("#00D7FA")+"|"+res
    i2=0
    print(fg("#00D7FA")+"--------------------------------------------------"+res)
    while(i2<8):
      if(ech[i3]=="p"):
        a="♟"
      elif(ech[i3]=="f"):
        a="♗"
      elif(ech[i3]=="t"):
        a="♖"
      elif(ech[i3]=="c"):
        a="♘"
      elif(ech[i3]=="r"):
        a="♔"
      elif(ech[i3]=="d"):
        a="♕"
      else:
        a=" "
      
      
      if(coordone[i3] in blanc):
        if(coordone[i3]in x):
          ligne=ligne+bg("#FF0000")+fg("#FFFFFF")+a.rjust(2).ljust(4)+res+res+fg("#00D7FA")+"|"+res
        else:
          ligne=ligne+fg("#FFFFFF")+a.rjust(2)+res+fg("#00D7FA")+"|".rjust(3)+res
        
      elif(coordone[i3] in noire):
        if(coordone[i3]in x):
          ligne=ligne+bg("#FF0000")+fg("#808080")+a.rjust(2).ljust(4)+res+fg("#00D7FA")+"|"+res
        
        else:
          ligne=ligne+fg("#808080")+a.rjust(2)+fg("#00D7FA")+"|".rjust(3)+res
        
    
      else:
        if(coordone[i3]in x):
          ligne=ligne+bg("#FF0000")+a.rjust(2).ljust(4)+res+fg("#00D7FA")+"|"+res
        else:
          ligne=ligne+a.rjust(2)+fg("#00D7FA")+"|".rjust(3)+res
        
      i3+=1
      i2+=1

    ligne=ligne+fg("#FF00C2") + chr(49+i).rjust(4)
    print (ligne)
    i+=1

  ligne=" ".ljust(4) +fg("#00D7FA")+"|"+res
  i=0
  # affichage des lettre
  print(fg("#00D7FA")+"--------------------------------------------------"+res)
  while(i<8):
    ligne=ligne+fg("#FF00C2")+chr(104-i).rjust(2)+res+fg("#00D7FA")+"|".rjust(3)+res
    i+=1
  print (ligne)
  switch(ech)
  

