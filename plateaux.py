from colored import fg, bg, attr


#tableau pour l'echiquier:
ech=["0"]*64

#coordone du tableau
coordone=[
    "a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8", 
    "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7",
    "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6", 
    "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5",
    "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4",
    "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3",
    "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2",
    "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"
    ]
print(coordone[63])
bordure=["a8","a7","a6","a5","a4","a3","a2","a1","h8","h7","h6","h5","h4","h3","h2","h1"]
bordureG=["a8","a7","a6","a5","a4","a3","a2","a1"]
bordureD=["h8","h7","h6","h5","h4","h3","h2","h1"]
switchBordureD= ["a8","a7","a6","a5","a4","a3","a2","a1"]
switchBordureG = ["h8","h7","h6","h5","h4","h3","h2","h1"]



def initech():
    a=["0"]*64
    return a
def plateau(tour):

    i=0
    ligne = "    "
    #couleur rose et gris
    color2= fg("#FF00C2")
    color1=fg("#00D7FA")
    
    res = attr('reset')

    
    # affichage des lettre
    while(i<8):
        ligne=ligne+color2+chr(97+i).rjust(3)+res
        i+=1
    print (ligne)

    

    i=0
    t=0
    l=0
    ligne=""
    
    print(ligne)
    
    while(i<8):
        j=0
        
        
        #Affichage des numero de ligne
        ligne=color2 + chr(56-i).ljust(4) +res 
        
        
       #affichage des element du plateaux 
        while(j<8):
          
          
          col= ech[t]
          
          if col == "0":
              ligne = ligne + color1 + ech[t].rjust(3)+ res
          else:
            ligne=ligne+ech[t]
          
          j+=1
          t+=1
          l+=1
         
        print(ligne)
        i+=1

def reverplateau():
    #inverse les coordone
    ech.reverse()
    coordone.reverse()
    print (coordone)

  
    i=0
    ligne = "    "
    #couleur rose et gris
    color2= fg("#FF00C2")
    color1=fg("#00D7FA")
    
    res = attr('reset')

    
    # affichage des lettre
    while(i<8):
        ligne=ligne+color2+chr(97+i).rjust(3)+res
        i+=1
    print (ligne)

    

    i=0
    t=0
    l=0
    ligne=""
    
    print(ligne)
    
    while(i<8):
        j=0
        
        
        #Affichage des numero de ligne
        ligne=color2 + chr(49+i).ljust(4) +res 
        
        
       #affichage des element du plateaux 
        while(j<8):
          
          
          col= ech[t]
          
          if col == "0":
              ligne = ligne + color1 + ech[t].rjust(3)+ res
          else:
            ligne=ligne+ech[t]
          
          j+=1
          t+=1
          l+=1
         
        print(ligne)
        i+=1


def switch(ech):
    ech.reverse()
    coordone.reverse()



