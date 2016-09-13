import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1234567',
                             db='veterinaria',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
'''
with connection.cursor() as cursor:
    sql = "INSERT INTO `usuario` (`username`, `pass`,`nombre`,`admin`,`foto`) VALUES (%s, %s,%s,%s,%s)"
    cursor.execute(sql, ('josdead', '1234','Jose Miguel Murillo R','1','a.jpg'))
    connection.commit()'''



