import os
try:
  from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
  from SocketServer import TCPServer as Server
except ImportError:
  from http.server import SimpleHTTPRequestHandler as Handler
  from http.server import HTTPServer as Server

# Read port selected by the cloud for our application
PORT = int(os.getenv('PORT', 8000))
# Change current directory to avoid exposure of control files

uri = "mongodb://admin:FHJWGTYRUNLADKWU@bluemix-sandbox-dal-9-portal.5.dblayer.com:20715,bluemix-sandbox-dal-9-portal.0.dblayer.com:20715/admin?ssl=true""

client = MongoClient()

client = MongoClient(uri)
print client

db = client.LCHAnlyzer
print db

ReadData = db.Test
ReadData_bpk = ReadData.find()
for doc in ReadData_bpk:
    print doc
os.chdir('static')

httpd = Server(("", PORT), Handler)
try:
  print("Start serving at port %i" % PORT)
  httpd.serve_forever()
except KeyboardInterrupt:
  pass
httpd.server_close()

