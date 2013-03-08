#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from pyramid.view import view_config
from botigaObjects import dadesProductes
from pyramid.httpexceptions import HTTPFound



here = os.path.dirname(os.path.abspath(__file__))  # --- direccio on es troba el fitxers tasks.py


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project':'botiga'}

@view_config(route_name='productes', renderer='productes.mako')
def productes_view(request):
    proj = "Botigueta Pro"
    #dades=dadesProductes(here)
    dades=dadesProductes()
    productes=dades.getProductes()
    return { "projecte":proj, "diccionari":productes }


@view_config(route_name='index', renderer='index.mako')
def inici_view(request):
    proj = "Botigueta Pro"
    menu = { 'Productes Disponibles' :'/botiga' , 'Les seves comandes':'/comandes' , 'Realitza la seva comanda':'/realitzar_comanda' }
    return {"projecte":proj, "menu":menu }

@view_config(route_name='comandes', renderer='comandes.mako')
def comandes_view(request):
    proj = "Botigueta Pro"
    #dades=dadesProductes(here)
    dades=dadesProductes()
    commandes=dades.getCommandes()
    return { "projecte":proj, "diccionari":commandes }
    

@view_config(route_name='realitzar_comanda', renderer='realitzar_comanda.mako')
def realitza_comanda_view(request):
    lista=[]
    proj = "Botigueta Pro"
    #dades=dadesProductes(here)
    dades=dadesProductes()
    productes=dades.getProductes()
    if request.method == 'POST':
        for prod in productes:
            if request.POST.get(prod)!='':
                #print request.POST.get(prod)
                lista.append(productes[prod]['Name'])
                lista.append(request.POST.get(prod))
                dades.escriu_dades_arxiu(lista)
                    #request.session.flash('New task was successfully added!')
            lista=[]
        return HTTPFound(location=request.route_url('comandes'))
            #else:
                #request.session.flash('Please enter a name for the task!')
    return {"projecte":proj, "diccionari":productes}
