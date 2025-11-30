import engDatabases.dbHandler as dbh

# Ejemplo de cómo agregar un material al database utilizando el database handler

database = 'data.db'
table = 'material'

# Material Input data
mat = 'AISI 4340'
fam = 'Metals'
subFam = 'Steels'
E = 205 #[GPa]
G = 80 #[GPa]
stressYield = 470 #[MPa]
stressUlt = 745 #[MPa]
strainPor = 22 #[%]
poisson = 0.29
density = 7.85 #[g/cm**3]
lengthUlt = 1*10**5 #[km]

# Units Conversion
E = E * 10**9 #[Pa]
G = G * 10**9 #[Pa]
stressYield = stressYield * 10**6 #[Pa]
stressUlt = stressUlt * 10**6 #[Pa]
strainPor = strainPor/100
density = density*1000 #[kg/m**3]
lengthUlt = lengthUlt*1000 #[m]


# Test Material insert manually
materialInput = [mat, fam, subFam,E,G,stressYield,stressUlt,strainPor,poisson,density,lengthUlt]

# dbh.addSingleRow(database, materialInput, table)



# dbh.updateSingleValue(database, table, "length_ult", '0.001', "material_name", "'AISI 4340'") # RECORDAR PONER VALORES DE COLUMNA EN STRING



dbh.showAll(database)
dbh.showTablesAndColumns()
