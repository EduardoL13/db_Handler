import engDatabases.dbHandler as dbh
import numpy as np
import pandas as pd
import sqlite3

def createDbTable(database, command):
    # Connect to database
    conn = sqlite3.connect(database)  
    # Cursor Creation
    c = conn.cursor() # Requisito necesario para crear tablas
    c.execute(command)
    # Command commit
    conn.commit()

    # Close connection
    conn.close()




# dbh.createDB('TestProyectWSA.db') # Línea de código para crear base de datos en el current proyect folder
database = 'TestProyectWSA'



# Leer tabla del DBR
table_df = pd.read_excel('DBR_Test.xlsx','WSA_00')

# Creación y llenado de vector de columnas de tabla
fileNameString = ("File Name","text")
keystringString = ("Keystring","text")
familyString = ("Family","text")
subfamilyString = ("Subfamily","text")
typeString = ("Type","text")

stringVector = [fileNameString,keystringString,familyString,subfamilyString,typeString]

file_name = table_df["File Name"]


# Creación de tabla dentro del database creado

# c.execute(""" CREATE TABLE design_input (
#     material_name text,  
#     family text,
#     sub_family text,
#     young_modulus real,
#     shear_modulus real,
#     yield_strength real,
#     ultimate_stress real,
#     strain_per real,
#     poisson real,
#     density real,    
#     length_ult real
#     )""")


# openCreateTable = dbh.createTableOpener("design_input")

table = "design_input" 

# commandExecute = openCreateTable

# for index, element in enumerate(stringVector):
    
#     if element == stringVector[-1]:
#         commandExecute += dbh.createTableClosing(element[0], element[1])
#     else:
#         commandExecute += element[0]
#         commandExecute += " "
#         commandExecute += element[1]
#         commandExecute += ","
        
# createDbTable(database, commandExecute)

tableCreated = dbh.dbExportToDataframe(database, table)


# PENDIENTE AÑADIR EL CONTENIDO DE LA TABLA
