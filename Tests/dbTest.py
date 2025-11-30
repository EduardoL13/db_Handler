
import sqlite3


# CREACIóN DE UNA TABLA de materiales:
# La idea es que este módulo cree la database para materiales y cargue las propiedades de los materiales (desde un cv) 
# 

#conn = sqlite3.connect(':memory')
conn = sqlite3.connect('data.db')

# Cursor Creation
c = conn.cursor() # Requisito necesario para crear tablas

mat = 'AISI 301'
fam = 'Metals'
subFam = 'Steels'
E = 193 #[GPa]
G = 71 #[GPa]
stressYield = 965 #[MPa]
stressUlt = 1257 #[MPa]
strainPor = 40 #[%]
poisson = 0.3
density = 8 #[g/cm**3]
lengthUlt = 16.2 #[km]

#Units Conversion
E = E * 10**9 #[Pa]
G = G * 10**9 #[Pa]
stressYield = stressYield * 10**6 #[Pa]
stressUlt = stressUlt * 10**6 #[Pa]
strainPor = strainPor/100
density = density*1000 #[kg/m**3]
lengthUlt = lengthUlt*1000 #[m]

# Table Creation

# c.execute(""" CREATE TABLE material (
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




# # Test Material insert manually
# materials_list = [(mat, fam, subFam,str(E),str(G),str(stressYield),str(stressUlt),str(strainPor),str(poisson),str(density),str(lengthUlt))]

# # Input data to table
# c.executemany("INSERT INTO material VALUES (?,?,?,?,?,?,?,?,?,?,?)", materials_list)


# # Delete data from table
# c.execute("DELETE from material WHERE rowid = '3' ")

# Query Data
c.execute("SELECT rowid, * FROM material WHERE sub_family = 'Aluminums' ")


listMats = c.fetchall()

for mat in listMats:
    print(mat)



# Command commit
conn.commit()

# Close connection
conn.close()



# Cómo borrar más de un elemento y por qué criterios?
# SELECT // FROM // WHERE // LIKE
