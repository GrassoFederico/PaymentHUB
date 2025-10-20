# Importa le dipendenze

from init import execute_query, execute_statement

import os
import cherrypy

cherrypy.config.update({'server.socket_port': 8090})
cherrypy.engine.restart()

class Web(object):
    @cherrypy.expose
    def index(self):
        return open('public/index.html')

@cherrypy.expose
class Tabelle(object):

    def GET(self):
        return execute_query('SHOW TABLES')

@cherrypy.expose
class Dati(object):

    def GET(self, tabella: str):
        return execute_query('SELECT * FROM `' + tabella + '`')

@cherrypy.expose
class Motore(object):
    
    def POST(self, nome: str, descrizione: str):
        execute_statement(
            'INSERT INTO `motore`(`nome`, `descrizione`) VALUES (:nome, :descrizione);',
            [{'nome': nome, 'descrizione': descrizione}]
        )

        raise cherrypy.HTTPRedirect("/", status=301)
    
    def PUT(self, ide: str, campo: str, valore: str):
        result = execute_statement(
            'UPDATE `motore` SET `' + campo + '` = :valore WHERE `id` = :id;',
            [{'valore': valore, 'id': ide}]
        )

        if (result): 
            return "Aggiornato".encode('utf8')
        else:
            return "Impossibile aggiornare".encode('utf8')
        
    def DELETE(self, ide: str):
        result = execute_statement(
            'DELETE FROM `motore` WHERE `id` = :id',
            [{'id': ide}]
        )

        if (result): 
            return "Cancellato".encode('utf8')
        else:
            return "Impossibile cancellare".encode('utf8')

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/tabelle': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        },
        '/dati': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        },
        '/motore': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        },
        '/assets': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public/assets'
        }
    }
    webapp = Web()
    webapp.tabelle = Tabelle()
    webapp.dati = Dati()
    webapp.motore = Motore()
    cherrypy.quickstart(webapp, '/', conf)