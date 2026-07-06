import mysql.connector as myconn

mydb = myconn.connect(
    host = "localhost",
    user = "root",
    password = "r00t1234",
    database = "mits"
    )

print(mydb,"connected successfully")



mycursor = mydb.cursor()


mycursor.execute("create table sdetails(name varchar(20),age int(3),contact bigint(10))")

print("table created successfully")

