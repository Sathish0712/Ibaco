#!C:/python/python.exe

import cgi
import mysql.connector

print("Content-Type:text/html\r\n\r\n")
print("<html>")
print("<body>")


Form=cgi.FieldStorage()
SName=Form.getvalue("Name")
SFlavour=Form.getvalue("Flavour")
SAddress=Form.getvalue("Address")
SContact=Form.getvalue("Contact")
SBranch=Form.getvalue("Branch")
print("<br><center><h2>Thank You for Ibaco Online Order<a href='/Ibaco'><br><br>Back To Home</a></h2></center>")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ibaco"
    )

mycursor=mydb.cursor()
sql="INSERT INTO customer(Name,Flavour,Address,Contact,Branch)VALUES(%s,%s,%s,%s,%s)"
val=(SName,SFlavour,SAddress,SContact,SBranch)
mycursor.execute(sql,val)
mydb.commit()


print("</body>")
print("</html>")
