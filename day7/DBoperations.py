insertquery = "insert into student values(104,'Neha',94,'vii')"
updatequery ="update student set sname =  'sugnya' where S_ID=103"
deletequery= "delete from student where S_ID=101"


import mysql.connector
con= mysql.connector.connect(host="localhost",port="3306",user="root",passwd="Mar@2011",database="mydb")
cors=con.cursor()
cors.execute(deletequery)
con.commit()
con.close()
print("Finished ............")

