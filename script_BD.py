import mysql.connector

HOST = input("Digite el HOST para la coneccion con MySQL o MariaDB ")
USER = input('Digite el USER para la coneccion con MySQL o MariaDB ')
PASSWORD = input('Digite el PASSWORD para la coneccion con MySQL o MariaDB ')

try:
    mysql = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD
    )
    cursor = mysql.cursor()

    cursor.execute("CREATE DATABASE MGFACT CHARACTER SET utf8")

except ValueError as e:
    print("Verifique los datos ingresados ")

