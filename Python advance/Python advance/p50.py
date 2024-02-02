import sqlite3
try:
    db=sqlite3.connect("fdb")
    cursor=db.cursor()
    sql="create table emp(empid int,empname varchar(50),salary int(10,2))"
    cursor.execute(sql)
    db.commit()
    db.close()
except Exception:
    print("Check Connection")
    
