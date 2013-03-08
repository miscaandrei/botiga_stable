import os

here = os.path.dirname(os.path.abspath(__file__))  # --- direccio on es troba el fitxers tasks.py

class dadesProductes(object):
    diccionari_productes={}
    diccionari_commandes={}
    
    def __init__(self):
        self.carrega_dades_arxiu()
    

    def carrega_dades_arxiu(self):
        
        #Codi funcional copiat des de la view
        llista_inicial=[]
        longitud_llista=0
        llista_temporal=[]
        diccionari={}
        proj = "Botigueta Pro"
        f=open(os.path.join(here, 'productes.txt'),'r')
        #f=open('productes.txt','r')
        for linia in f:
            llista_inicial.append(linia.strip())
        f.close()
        longitud_llista=len(llista_inicial)
        for x in range(0, longitud_llista):
            llista_temporal=llista_inicial[x].split('    ')
            diccionari.update({llista_temporal[0]:{'Name':llista_temporal[1], 'Stock':llista_temporal[2],'Price':llista_temporal[3]}})
            llista_temporal=[]
        f.close()
        #Final Codi copiat
        
        self.diccionari_productes=diccionari
    
    def getProductes(self):
        return self.diccionari_productes


    def escriu_dades_arxiu(self,lista_valors,numero_commanda):
        f=open(os.path.join(here, 'commandes.txt'),'a')
        f.write(numero_commanda)
        f.write('    ')
        f.write(lista_valors[0])
        f.write('    ')
        f.write(lista_valors[1])
        f.write('\n')
    
    def getCommandes(self):
        #Codi funcional copiat des de la view
        llista_inicial=[]
        longitud_llista=0
        llista_temporal=[]
        diccionari={}
        proj = "Botigueta Pro"
        f=open(os.path.join(here, 'commandes.txt'),'r')
        #f=open('productes.txt','r')
        for linia in f:
            llista_inicial.append(linia.strip())
        f.close()
        longitud_llista=len(llista_inicial)
        for x in range(0, longitud_llista):
            #print llista_inicial[x]
            llista_temporal=llista_inicial[x].split('    ')
            diccionari.update({x:{'ID_Commanda':llista_temporal[0], 'Nom':llista_temporal[1],'Quantitat':llista_temporal[2]}})
            llista_temporal=[]
        f.close()
        #Final Codi copiat
        return diccionari
    
    
    def getNumeroCommanda(self):
        #Codi funcional copiat des de la view
        llista_inicial=[]
        longitud_llista=0
        llista_temporal=[]
        llista_final=[]
        diccionari={}
        proj = "Botigueta Pro"
        f=open(os.path.join(here, 'commandes.txt'),'r')
        #f=open('productes.txt','r')
        for linia in f:
            llista_inicial.append(linia.strip())
        f.close()
        longitud_llista=len(llista_inicial)
        for x in range(0, longitud_llista):
            #print llista_inicial[x]
            llista_temporal=llista_inicial[x].split('    ')
            llista_final.append(int(llista_temporal[0]))
            llista_temporal=[]
        f.close()
        #Final Codi copiat
        llista_final.sort()
        return  llista_final.pop()


d=dadesProductes()
numero=d.getNumeroCommanda()
print numero
'''
# TEST
d=dadesProductes()
producte=d.getProductes()

for element in producte:
    print element
    print producte[element]


lista=['Marocacuca','4']
d=dadesProductes()
producte=[]
producte=d.escriu_dades_arxiu(lista)


d=dadesProductes()
producte=d.getCommandes()

for element in producte:
    print element
    print producte[element]
'''
