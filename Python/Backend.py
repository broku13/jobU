from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/internships.json',methods = ['GET'])
def login():
   if request.method == 'GET':
      

if __name__ == '__main__':
   app.run(debug = True)