# Importa le dipendenze

from init import execute_query, execute_statement

import os
import cherrypy

cherrypy.config.update({'server.socket_port': 8080})
cherrypy.engine.restart()

class Web(object):
    @cherrypy.expose
    def index(self, tabella):
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

        raise cherrypy.HTTPRedirect("/?tabella=motore", status=301)
    
    def PUT(self, ide: str, campo: str, valore: str):
        result = execute_statement(
            'UPDATE `motore` SET `' + campo + '` = :valore WHERE `id` = :id;',
            [{'valore': valore, 'id': ide}]
        )

        if (result): 
            return '{"message": "Aggiornato"}'.encode('utf8')
        else:
            return '{"message": "Impossibile aggiornare"}'.encode('utf8')
        
    def DELETE(self, ide: str):
        result = execute_statement(
            'DELETE FROM `motore` WHERE `id` = :id',
            [{'id': ide}]
        )

        if (result): 
            return '{"message": "Cancellato"}'.encode('utf8')
        else:
            return '{"message": "Impossibile cancellare"}'.encode('utf8')

@cherrypy.expose
class Nazione(object):
    
    def POST(self, codice_2_caratteri: str, codice_3_caratteri: str, codice_numerico: str):
        execute_statement(
            'INSERT INTO `nazione`(`codice_2_caratteri`, `codice_3_caratteri`, `codice_numerico`) VALUES (:codice_2_caratteri, :codice_3_caratteri, :codice_numerico);',
            [{'codice_2_caratteri': codice_2_caratteri, 'codice_3_caratteri': codice_3_caratteri, 'codice_numerico': codice_numerico}]
        )

        raise cherrypy.HTTPRedirect("/?tabella=nazione", status=301)
    
    def PUT(self, ide: str, campo: str, valore: str):
        result = execute_statement(
            'UPDATE `nazione` SET `' + campo + '` = :valore WHERE `id` = :id;',
            [{'valore': valore, 'id': ide}]
        )

        if (result): 
            return '{"message": "Aggiornato"}'.encode('utf8')
        else:
            return '{"message": "Impossibile aggiornare"}'.encode('utf8')
        
    def DELETE(self, ide: str):
        result = execute_statement(
            'DELETE FROM `nazione` WHERE `id` = :id',
            [{'id': ide}]
        )

        if (result): 
            return '{"message": "Cancellato"}'.encode('utf8')
        else:
            return '{"message": "Impossibile cancellare"}'.encode('utf8')

@cherrypy.expose
class Pagamento(object):
    
    def POST(self, nome: str, descrizione: str, attivo: str = False):
        execute_statement(
            'INSERT INTO `pagamento`(`nome`, `descrizione`, `attivo`) VALUES (:nome, :descrizione, :attivo);',
            [{'nome': nome, 'descrizione': descrizione, 'attivo': attivo}]
        )

        raise cherrypy.HTTPRedirect("/?tabella=pagamento", status=301)
    
    def PUT(self, ide: str, campo: str, valore: str):
        result = execute_statement(
            'UPDATE `pagamento` SET `' + campo + '` = :valore WHERE `id` = :id;',
            [{'valore': valore, 'id': ide}]
        )

        if (result): 
            return '{"message": "Aggiornato"}'.encode('utf8')
        else:
            return '{"message": "Impossibile aggiornare"}'.encode('utf8')
        
    def DELETE(self, ide: str):
        result = execute_statement(
            'DELETE FROM `pagamento` WHERE `id` = :id',
            [{'id': ide}]
        )

        if (result): 
            return '{"message": "Cancellato"}'.encode('utf8')
        else:
            return '{"message": "Impossibile cancellare"}'.encode('utf8')

@cherrypy.expose
class Rotta(object):
    
    def POST(self, successo: str, annullamento: str, webhook: str, pagina_pagamento: str):
        execute_statement(
            'INSERT INTO `rotta`(`successo`, `annullamento`, `webhook`, `pagina_pagamento`) VALUES (:successo, :annullamento, :webhook, :pagina_pagamento);',
            [{'successo': successo, 'annullamento': annullamento, 'webhook': webhook, 'pagina_pagamento': pagina_pagamento}]
        )

        raise cherrypy.HTTPRedirect("/?tabella=rotta", status=301)
    
    def PUT(self, ide: str, campo: str, valore: str):
        result = execute_statement(
            'UPDATE `rotta` SET `' + campo + '` = :valore WHERE `id` = :id;',
            [{'valore': valore, 'id': ide}]
        )

        if (result): 
            return '{"message": "Aggiornato"}'.encode('utf8')
        else:
            return '{"message": "Impossibile aggiornare"}'.encode('utf8')
        
    def DELETE(self, ide: str):
        result = execute_statement(
            'DELETE FROM `rotta` WHERE `id` = :id',
            [{'id': ide}]
        )

        if (result): 
            return '{"message": "Cancellato"}'.encode('utf8')
        else:
            return '{"message": "Impossibile cancellare"}'.encode('utf8')

@cherrypy.expose
class Versione(object):
    
    def POST(self, crea_pagamento: str, recupera_pagamento: str, esegui_pagamento: str, verifica_pagamento: str):
        execute_statement(
            'INSERT INTO `versione`(`crea_pagamento`, `recupera_pagamento`, `esegui_pagamento`, `verifica_pagamento`) VALUES (:crea_pagamento, :recupera_pagamento, :esegui_pagamento, :verifica_pagamento);',
            [{'crea_pagamento': crea_pagamento, 'recupera_pagamento': recupera_pagamento, 'esegui_pagamento': esegui_pagamento, 'verifica_pagamento': verifica_pagamento}]
        )

        raise cherrypy.HTTPRedirect("/?tabella=versione", status=301)
    
    def PUT(self, ide: str, campo: str, valore: str):
        result = execute_statement(
            'UPDATE `versione` SET `' + campo + '` = :valore WHERE `id` = :id;',
            [{'valore': valore, 'id': ide}]
        )

        if (result): 
            return '{"message": "Aggiornato"}'.encode('utf8')
        else:
            return '{"message": "Impossibile aggiornare"}'.encode('utf8')
        
    def DELETE(self, ide: str):
        result = execute_statement(
            'DELETE FROM `versione` WHERE `id` = :id',
            [{'id': ide}]
        )

        if (result): 
            return '{"message": "Cancellato"}'.encode('utf8')
        else:
            return '{"message": "Impossibile cancellare"}'.encode('utf8')

@cherrypy.expose
class URL(object):
    
    def POST(self, id_rotta: str, id_versione: str, id_nazione: str, id_pagamento: str, id_motore: str, meta: str, test: str = False):
        execute_statement(
            'INSERT INTO `url`(`id_rotta`, `id_versione`, `id_nazione`, `id_pagamento`, `id_motore`, `meta`, `test`) VALUES (:id_rotta, :id_versione, :id_nazione, :id_pagamento, :id_motore, :meta, :test);',
            [{'id_rotta': id_rotta, 'id_versione': id_versione, 'id_nazione': id_nazione, 'id_pagamento': id_pagamento, 'id_motore': id_motore, 'meta': meta, 'test': test}]
        )

        raise cherrypy.HTTPRedirect("/?tabella=url", status=301)
    
    def PUT(self, ide: str, campo: str, valore: str):
        result = execute_statement(
            'UPDATE `url` SET `' + campo + '` = :valore WHERE `id` = :id;',
            [{'valore': valore, 'id': ide}]
        )

        if (result): 
            return '{"message": "Aggiornato"}'.encode('utf8')
        else:
            return '{"message": "Impossibile aggiornare"}'.encode('utf8')
        
    def DELETE(self, ide: str):
        result = execute_statement(
            'DELETE FROM `url` WHERE `id` = :id',
            [{'id': ide}]
        )

        if (result): 
            return '{"message": "Cancellato"}'.encode('utf8')
        else:
            return '{"message": "Impossibile cancellare"}'.encode('utf8')
        
@cherrypy.expose
class Select(object):
    
    def POST(self, campo: str, tabella: str):
        return execute_query('SELECT `id`, `' + campo + '` AS `campo` FROM `' + tabella + '`')

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
        '/nazione': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        },
        '/pagamento': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        },
        '/rotta': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        },
        '/versione': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        },
        '/url': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        },
        '/select': {
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
    webapp.nazione = Nazione()
    webapp.pagamento = Pagamento()
    webapp.rotta = Rotta()
    webapp.versione = Versione()
    webapp.url = URL()
    webapp.select = Select()
    cherrypy.quickstart(webapp, '/', conf)