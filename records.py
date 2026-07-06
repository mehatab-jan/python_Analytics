import mysql.connector as myconn

mydb = myconn.connect(
    host = "localhost",
    user = "root",
    password = "r00t1234",
    database = "mits"
    )

print(mydb,"connected successfully")



mycursor = mydb.cursor()

sql = "insert into sdetails(name,age,contact) values(%s,%s,%s)"

values = ("mehatab",20,7569897579)

mycursor.execute(sql,values)
mydb.commit()

mycursor.execute("select * from sdetails")
result = mycursor.fetchall()

for i in result:
    print(i)