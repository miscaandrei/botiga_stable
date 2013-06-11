#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from pyramid.view import view_config
from botigaObjects import dadesProductes
from pyramid.httpexceptions import HTTPFound



from pyramid.view import (
    view_config,
    forbidden_view_config,
    )

from pyramid.security import (
    remember,
    forget,
    authenticated_userid,
    )

from .security import USERS
from .security import comprova_usuari



here = os.path.dirname(os.path.abspath(__file__))  # --- direccio on es troba el fitxers tasks.py


@view_config(route_name='home', renderer='index.mako')
def my_view(request):
    proj = "Botigueta Pro"
    menu = { 'Productes Disponibles' :'/botiga' , 'Les seves comandes':'/comandes' , 'Realitza la seva comanda':'/realitzar_comanda' }
    return {"projecte":proj, "menu":menu }
    
@view_config(route_name='productes', renderer='productes.mako')
def productes_view(request):
    proj = "Botigueta Pro"
    #dades=dadesProductes(here)
    dades=dadesProductes()
    productes=dades.getProductes()
    return { "projecte":proj, "diccionari":productes, 'logged_in':authenticated_userid(request)  }


@view_config(route_name='index', renderer='index.mako')
def inici_view(request):
    proj = "Botigueta Pro"
    menu = { 'Productes Disponibles' :'/botiga' , 'Les seves comandes':'/comandes' , 'Realitza la seva comanda':'/realitzar_comanda' }
    return {"projecte":proj, "menu":menu }

@view_config(route_name='comandes', renderer='comandes.mako', permission='commandes')
def comandes_view(request):
    proj = "Botigueta Pro"
    #dades=dadesProductes(here)
    dades=dadesProductes()
    commandes=dades.getCommandes()
    return { "projecte":proj, "diccionari":commandes, 'logged_in':authenticated_userid(request)  }
    

@view_config(route_name='realitzar_comanda', renderer='realitzar_comanda.mako',	permission='make_commanda')
def realitza_comanda_view(request):
    lista=[]
    proj = "Botigueta Pro"
    #dades=dadesProductes(here)
    dades=dadesProductes()
    productes=dades.getProductes()
    numero_pedido=str(dades.getNumeroCommanda())
    if request.method == 'POST':
        for prod in productes:
            if request.POST.get(prod)!='':
                #print request.POST.get(prod)
                lista.append(productes[prod]['Name'])
                lista.append(request.POST.get(prod))
                dades.escriu_dades_arxiu(lista,numero_pedido)
                    #request.session.flash('New task was successfully added!')
            lista=[]
        return HTTPFound(location=request.route_url('comandes'))
            #else:
                #request.session.flash('Please enter a name for the task!')
    return {"projecte":proj, "diccionari":productes, 'logged_in':authenticated_userid(request)  }





@view_config( route_name='login', renderer='login.mako')

@forbidden_view_config(renderer='login.mako')
def login(request):
    login_url = request.route_url('login')
    # detectem des de quina URL ve el visitant
    referrer = request.url
    # retornem l'usuari a la home page si ha vingut directe al login
    if referrer == login_url:
        referrer = '/' # never use the login form itself as came_from
    came_from = request.params.get('came_from', referrer)
    user = authenticated_userid(request)
    if user:
        lloc = came_from.split("/")
        message = "Els usuaris %s no tenen permis a accedir a %s!" % (user,lloc[len(lloc)-1])
    else:
        message = "Cal indentificar-se per accedir a aquest apartat"
    login = ''
    password = ''
    if 'form.submitted' in request.params:
        login = request.params['login']
        password = request.params['password']
        if comprova_usuari(login,password):
            headers = remember(request, login)
            return HTTPFound(location = came_from,
                             headers = headers)
        message = 'Failed login'

    return dict(
        message = message,
        url = request.application_url + '/login',
        came_from = came_from,
        login = login,
        password = password,
        user = authenticated_userid(request), # afegim usuari autenticat si l'hi ha
        )
    

@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location = request.route_url('home'),
                     headers = headers)
                     
