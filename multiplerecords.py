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

values = [
    ("musaveer",19,8317550106),
    ("mohammad",17,6789654321)
]
mycursor.executemany(sql,values)
mydb.commit()

mycursor.execute("select * from sdetails")
result = mycursor.fetchall()

for i in result:
    print(i)