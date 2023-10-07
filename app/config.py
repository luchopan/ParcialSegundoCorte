import pyodbc

# Configuración de la conexión a la base de datos Access
connection = pyodbc.connect(
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\LUIS\Documents\VS CODE\myprojectweb\app\TaskBD.accdb;'
)

cursor = connection.cursor()
