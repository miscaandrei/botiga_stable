import os

here = os.path.dirname(os.path.abspath(__file__))  # --- direccio on es troba el fitxers tasks.py

class dadesProductes(object):
    diccionari_productes={}
    
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

'''
# TEST
d=dadesProductes()
producte=d.getProductes()

for element in producte:
    print element
    print producte[element]
'''
