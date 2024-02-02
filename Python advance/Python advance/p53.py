import sqlite3
try:
    db=sqlite3.connect("xyz")
    cursor=db.cursor()
    a=int(input("Enter the empID\n"));
    b=(input("Enter the empname\n"));
    c=float(input("Enter the salary\n"))
    sql="insert into emp values('"+str(a)+"','"+b+"','"+str(c)+"')"
    cursor.execute(sql)
    db.commit()
    print("Record Inserted Successfully")
    db.close()
except Exception:
    print("Check Connection")
    
