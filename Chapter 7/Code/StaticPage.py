import cherrypy
 
class StaticPage():
     
     @cherrypy.expose
     def index(self):
         return open('static.html')
        
        
if __name__== '__main__':
    cherrypy.quickstart(StaticPage())