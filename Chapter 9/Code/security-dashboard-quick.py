import cherrypy
from SecurityDataQuick import SecurityData

class SecurityDashboard:
    
    def __init__(self, securityData):
        self.securityData = securityData
    
    @cherrypy.expose
    def index(self):
        return """
               <!DOCTYPE html>
                <html lang="en">

                <head>
                    <title>Home Security Dashboard</title>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <meta http-equiv="refresh" content="2">
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css">
                    <link rel="stylesheet" href="led.css">
                    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js"></script>
                    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js"></script>
                    <style>
                        .element-box {
                            border-radius: 10px;
                            border: 2px solid #C8C8C8;
                            padding: 20px;
                        }

                        .card {
                            width: 600px;
                        }

                        .col {
                            margin: 10px;
                        }
                    </style>
                </head>

                <body>
                    <div class="container">
                        <br/>
                        <div class="card">
                             <div class="card-header">
                                <h3>Home Security Dashboard</h3>
                             </div>
                             <div class="card-body">
                                <div class="row">
                                    <div class="col element-box">
                                        <h4>Armed</h4>
                                        <div class = """ + self.securityData.getArmedStatus() + """></div>
                                    </div>
                                    <div class="col element-box">
                                        <h4>Status</h4>
                                        <p>""" + self.securityData.getAlarmStatus() + """</p>
                                    </div>
                                    <div class="col element-box">
                                        <h4>Last Check:</h4>
                                        <p>""" + self.securityData.getTime() + """</p>
                                    </div>
                                </div>
                            </div>
                            <div class="card-footer" align="center">
                                <img src=""" + self.securityData.getSecurityImage() + """/>
                                <p>""" + self.securityData.getDetectedMessage() + """</p>
                            </div>
                        </div>
                    </div>
                </body>

                </html>
               """
    
if __name__=="__main__":
    securityData = SecurityData()
    conf = {
        '/led.css':{
            'tools.staticfile.on': True,
            'tools.staticfile.filename': '/home/pi/styles/led.css'
            },
        '/intruder.png':{
            'tools.staticfile.on': True,
            'tools.staticfile.filename': '/home/pi/images/intruder.png'
            },
        '/all-clear.png':{
            'tools.staticfile.on': True,
            'tools.staticfile.filename': '/home/pi/images/all-clear.png'
            },
        '/not-armed.png':{
            'tools.staticfile.on': True,
            'tools.staticfile.filename': '/home/pi/images/not-armed.png'
            }
    }
    cherrypy.quickstart(SecurityDashboard(securityData),'/',conf)
    
    
    

    