import sqlite3
try:
    db=sqlite3.connect("xyz")
    cursor=db.cursor()
    while(True):
        a=int(input("Enter the empID\n"))
        b=(input("Enter the empname\n"))
        c=float(input("Enter the salary\n"))
        sql="insert into emp values('"+str(a)+"','"+b+"','"+str(c)+"')"
        cursor.execute(sql)
        db.commit();
        x=input("Do you want to continue? Press Y to continue N to Stop\n")
        if(x=="n" or x=="N"):
            break
    print("Record Inserted Successfully")
    db.close()
except Exception:
    print("Check correction")
    
