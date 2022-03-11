import pymysql
from base64 import b64encode
conn = pymysql.connect(
      host= "database-3.c6ojy4yqq7gm.us-east-2.rds.amazonaws.com",
        user = "admin",
        password = "Kingmaker007",
        port = 3306
        )

def insert_details(fName, lName,email,password):
    cur=conn.cursor()
    cur.execute("INSERT INTO AWS_TEAM8_DATABASE.USER_REGISTRATION_INFO(FIRST_NAME,LAST_NAME,EMAIL,PASSWORD) VALUES (%s,%s,%s,%s)", (fName, lName,email,password))
    conn.commit()

def get_details():
    cur=conn.cursor()
    cur.execute("SELECT *  AWS_TEAM8_DATABASE.USER_REGISTRATION_INFO")
    details = cur.fetchall()
    return details

def get_email_password_details():
    cur=conn.cursor()
    cur.execute("SELECT EMAIL,PASSWORD FROM AWS_TEAM8_DATABASE.USER_REGISTRATION_INFO")
    User_deatils = cur.fetchall()
    return User_deatils

def get_image():
    cur=conn.cursor()
    #print('---------------------------------------------'+location+'--------------------------------------------------------------')
    cur.execute("SELECT HOTEL_IMAGE FROM AWS_TEAM8_DATABASE.ABHI_HOTEL_DATABSE"  )
    #cur.execute("SELECT HOTEL_IMAGE,HOTEL_DISCRIPTION,HOTEL_START_PRICE FROM AWS_TEAM8_DATABASE.HOTEL_INFO_TABLE WHERE HOTEL_LOCATION = "+" "+"'"+ str(location)+"'")
    Image_file = cur.fetchall()
    return  Image_file