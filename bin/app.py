# Importa le dipendenze

from init import execute_query

import cherrypy

cherrypy.config.update({'server.socket_port': 8080})
cherrypy.engine.restart()


@cherrypy.expose
class StringGeneratorWebService(object):

    def GET(self):
        return execute_query('SHOW TABLES')
        

    # def POST(self, length=8):
    #     some_string = ''.join(random.sample(string.hexdigits, int(length)))
    #     cherrypy.session['mystring'] = some_string
    #     return some_string

    # def PUT(self, another_string):
    #     cherrypy.session['mystring'] = another_string

    # def DELETE(self):
    #     cherrypy.session.pop('mystring', None)

if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        }
    }
    cherrypy.quickstart(StringGeneratorWebService(), '/', conf)