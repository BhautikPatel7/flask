from flask import *
app = Flask(__name__)

@app.route('/')  
def message():  
      return render_template('message.html')
      
@app.route('/hello/<name>')
def hello(name): 
    return "Hello %s!" %name

@app.route('/admin')
def admin(admin):
    return f"hello super user {admin}"

@app.route('/guest/<username>')
def greetUSer(username):
    return {"message":f"hello guest {username}"}

@app.route("/user/<username>")
def hellouser(username) :
    if username == "admin" : 
        return {"message" : f"hello admin welcomecack"}
    else :
        return {"message" : f"hey guest"}
    
@app.route('/login', methods = ["GET"])
def login():
    uname=request.args.get['uname']
    passwrd=request.args.get['pass']  
    if uname=="ayush" and passwrd=="google":  
        return "Welcome %s" %uname   

if __name__ == "__main__":
    app.run(debug = True)