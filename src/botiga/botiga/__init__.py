#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from .security import groupfinder
from pyramid.config import Configurator
from .models import RootFactory

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    import os
    import models 
    here = os.path.dirname(os.path.abspath(__file__))
    settings['mako.directories'] = os.path.join(here, 'templates')
    config = Configurator(settings=settings)

    config = Configurator(settings=settings,root_factory='.models.RootFactory')


    authn_policy = AuthTktAuthenticationPolicy('sosecret', callback=groupfinder, hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    config = Configurator(settings=settings,root_factory='.models.RootFactory')
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    
    
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('index', '/index')  # nova
    config.add_route('productes', '/botiga')  # productes = ruta fisica de la view , /botiga=URL del navegador
    config.add_route('comandes', '/comandes')  # nova
    config.add_route('realitzar_comanda', '/realitzar_comanda')  # nova
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.scan()
    return config.make_wsgi_app()
