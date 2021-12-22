import pymysql

def obtener_conexion():
    return pymysql.connect(host = '192.168.194.22', user = 'win', password = '12345', db= 'alimentosdataset', port = 3306)