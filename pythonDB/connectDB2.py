import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Puffyfish",
  database = "mydatabase"
)

mycursor = mydb.cursor()

# GET INPUT FROM USER
userInput = ("")
val = []


while userInput != 'x':
  # Setup SQL Insert
  sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
  # Get user input
  userInput = input("Welcome to the database!\n"
       "Please select one of the following:\n" 
       "1 to enter a record\n"
       "C to commit the record/records\n"
       "S to search for a record\n"
       "A to display in ascending order\n"
       "D to display in descending order\n"
       "U to clear records")
  if userInput == '1':
    # Get input name and address
    inpName = input("Enter record name\n")
    inpAddress = input("Enter record address\n")
    val.append((inpName, inpAddress))
  elif userInput == 'c'.upper:
    # commit data to database
    mycursor.executemany(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.\n")
    val = []
  
  elif userInput == 's'.upper:
    sInput = input("Do you want to search by name, address or id?\n")
    if sInput == "name":
      name = input("Type in the name you're looking for: ")
      SELECT

  elif userInput == 'u'.upper:
    val = []
    print("Uncommited records cleared\n")
  