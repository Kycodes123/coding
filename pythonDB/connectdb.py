import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "Puffyfish",
    database  = "mydatabase"
)


#creating a new database once
mycursor = mydb.cursor()

#INSERT DATA INTO DATABASE
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#mycursor.execute(sql)
val =   [("Sarah Jane", "1 Lost Street"),
        ("John Doe", "2 Lost Street"),
        ("Batman", "Cave"),
        ("John Doe", "2 Lost Street"),
        ("Peter Parker","High building"),
        ("Santa", "NorthPole")
        ]


mycursor.executemany(sql, val)
mydb.commit()
#print(mycursor.rowcount, "record inserted")

#ALTER A TABLE
#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")



# mycursor.execute("""CREATE TABLE customers(
# name VARCHAR(255),
# address VARCHAR(255))""")

#print(mydb)