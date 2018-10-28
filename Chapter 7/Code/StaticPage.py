import cherrypy
 
class StaticPage():
     
     @cherrypy.expose
     def index(self):
         return open('static.html')
        
cherrypy.quickstart(StaticPage())