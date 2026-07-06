import mysql.connector as myconn

mydb = myconn.connect(
    host = "localhost",
    user = "root",
    password = "r00t1234"
    )

print(mydb,"connected successfully")



mycursor = mydb.cursor()
mycursor.execute("show databases")

for i in mycursor:
    print(i)

