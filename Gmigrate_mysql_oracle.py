import cx_Oracle
import mysql.connector as mysql

try:
    #Connect to Mysql Database
    mySQLCon = mysql.connect(host="<hostname>",    
                     user="<user>",         
                     password="<password>", 
                     database="<dbname>",
                     port="<port_number>")  
    print("Connected to MySql DB", mySQLCon.get_server_info())
    cur=mySQLCon.cursor()
    query=("SELECT DATE_FORMAT(DATETIMECREATED, '%Y-%m-%d %H.%i.%s'),COL2,COL3 FROM <TABLE_NAME>")
    cur.execute(query)
    myresult=cur.fetchall()
    for var in myresult:
        date=var[0]
        cameraid=var[1]
        faceid=var[2]
    
    print("Data Fetched from mysql")
        
except Exception as e:
    print("MySQL Database Error",e)

#Connect to Oracle Database
try:
    dsn_con=cx_Oracle.makedsn('<hostname>','<port_number>',service_name='<service_name>')
    con=cx_Oracle.connect(user=r'<user>',password=r'<password>',dsn=dsn_con)
    print("Connected to Oracle Database",con.version)
    cur=con.cursor()
#     query1=("INSERT INTO GOLDENEYE (DATETIMECREATED,CAMERAID,FACEIDAWS) VALUES(to_date('"+date+"', 'yyyy/mm/dd hh24:mi:ss'),'"+cameraid+"','"+faceid+"')")
#     cur.execute(query2)
#     con.commit()
#     print("Data Inserted")
    
    query2=("SELECT * FROM GOLDENEYE")
    cur.execute(query2)
    data=cur.fetchall()
    
    for result in data: 
        print(result)

except Exception as e:
    print("Oracle Database Error",e)