
from flask import Flask, render_template, request, flash, redirect,url_for, jsonify, session 
from flask import Response,send_file
app = Flask(__name__)
import pymysql
import rds_db as db
from base64 import b64encode
@app.route('/',methods=['POST','GET'])
def home():
    details = db.get_image()
    image_list = []
    for i in details:
            images = b64encode(i[0]).decode("utf-8")
            image_list.append(images)
    return render_template('home.html',data = image_list)


@app.route('/login')
def index():
    return render_template('login.html')



@app.route('/loginInfo',methods = ['POST','GET'])
def login():  
    if request.method == 'POST':
        email_html = request.form['email']
        password_html = request.form['password']
        User_details = db.get_email_password_details()
        for i in User_details:
               emails_temp = (i[0])
               password_temp = (i[1])
               if email_html == emails_temp and password_html == password_temp :
                return 'Welcome'
        return render_template("wrongpwd.html")    

     
     
            
    
@app.route('/signup')
def signup():
    return render_template('registration.html')

@app.route('/registrationInfo',methods = ['POST','GET'])
def registration():
    if request.method == 'POST':
        fName = request.form['fName']
        lName = request.form['lName']
        email = request.form['email']
        password = request.form['password']
        db.insert_details(fName, lName,email,password)
        return render_template("regSuc.html")

@app.route('/image_display',methods = ['POST','GET'])
def Index1():
    details = db.get_image
    if request.method == 'GET':   
            image_list = []
            for i in details:
                    images = b64encode(i[0]).decode("utf-8")
                    image_list.append(images)
    return render_template('home.html', data = image_list)
 

if __name__ == "__main__":
    
    app.run(debug=True)