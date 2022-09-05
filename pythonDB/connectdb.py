import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Puffyfish"

)
#creating a new database once
mycursor = mydb.cursor()

mycursor.execute()

#print(mydb)