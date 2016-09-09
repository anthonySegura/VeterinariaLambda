import pymysql
from usuarios import usuarios

connection = pymysql.connect(host='186.15.106.226',
                             user='anthony',
                             password='1234567',
                             db='veterinaria',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


"""with connection.cursor() as cursor:
    sql = "INSERT INTO `usuario` (`username`, `pass`,`nombre`,`admin`,`foto`) VALUES (%s, %s,%s,%s,%s)"
    cursor.execute(sql, ('josdead', '1234','Jose Miguel Murillo R','1','a.jpg'))
    connection.commit()"""

users=[]
def obtenerUsuarios():
    with connection.cursor() as cursor:
        sql = "SELECT `*` FROM `usuario`"
        cursor.execute(sql)
        x=cursor.fetchone()
        while(x!=None):
            usuariotemp=usuarios(x['username'],x['nombre'],x['pass'],x['foto'],x['admin'])
            users.append(usuariotemp)
            x=cursor.fetchone()

obtenerUsuarios()
print(len(users))


