import sqlite3

# PENDIENTE AGREGAR LOS DATABASES Y VINCULAR LOS TABLENAMES A CADA DATABASE

tablesNames = {'materials':('material_name text','family text','sub_family text ',
                            'young_modulus real','shear_modulus real','yield_strength real','ultimate_stress real',
                            'strain_per real','poisson real', 'density real', 'length_ult real')}


def showAll(dataBase): # Para futuro ponerle opción de deshabilitar id
    """
    Description:
    Show  full database with id rows

    Parameters: desired database

    Output: none (printed database)
    """    
    # Connect to database
    conn = sqlite3.connect(dataBase)
    # Cursor Creation
    c = conn.cursor() # Requisito necesario para crear tablas
    c.execute("SELECT rowid, * FROM material")

    listMats = c.fetchall()

    for mat in listMats:
        print(mat)

    # Command commit
    conn.commit()

    # Close connection
    conn.close()

def addSingleRow(dataBase,row,table): # Mirar si hay forma de extraer la tabla directamente desde el parámetro "dataBase"
    """
    Description:
    Add a row of elements to a specified database

    Parameters: 
    desired database (dataBase)
    desired row (row) Type: List of values for each column
    desired table (table)

    Output: none (printed updated database)
    """       
    # Connect to database
    conn = sqlite3.connect(dataBase)
    # Cursor Creation
    c = conn.cursor() # Requisito necesario para crear tablas
    
    stringRow = [str(x) for x in row] # list with each element as string

    stringInput = "("
    
    for element in stringRow:
        if len(stringInput) == 1:
            stringInput = stringInput + "'" +  element + "'"
        else:
            stringInput = stringInput + "," + "'" + element + "'"

    stringInput = stringInput + ")"     

    c.execute("INSERT INTO " + table + " VALUES " + stringInput )
    
    # Command commit
    conn.commit()
    
    # Close Connection
    conn.close()
    
def updateSingleValue(dataBase,table,colValue,value,rowID,rowValue): # PENDIENTE IMPLEMENTAR MANERA DE VERIFICAR QUE EL VALOR SE HAYA AGREGADO CORRECTAMENRE
    """
    Description:
    Upadtes a single cell value within an existing column by giving a rowId to a specified database

    Parameters: 
    desired database (dataBase)
    desired table (table)
    column where value to be updated is located (colValue)
    desired value for update (value)
    identification for locating row which row has the value to be updated (rowID)
    new Value to be updated in located cell (cellValue)

    Output: none (printed updated database)
    """   
    # Connect to database
    conn = sqlite3.connect(dataBase)
    # Cursor Creation
    c = conn.cursor() # Requisito necesario para crear tablas
    

    c.execute("UPDATE " + table + " SET " + colValue + " = " + value + " WHERE " + rowID + " = " + rowValue  )
    
    # Command commit
    conn.commit()
    
    # Close Connection
    conn.close()   
    
def showTablesAndColumns():
    """
    Description: Displays available tables and columns 

    Returns
    -------
    None.

    """
    print("Table Name and Columns: ", tablesNames)
    
    
    
    
