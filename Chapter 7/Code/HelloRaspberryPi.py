import cherrypy
 
class HelloWorld():
     
     @cherrypy.expose
     def index(self):
         return "Hello Raspberry Pi!"
        
        
cherrypy.quickstart(HelloWorld())