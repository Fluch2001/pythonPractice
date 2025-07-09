class consulta:
    #sentencias SQL en String

    createTable = '''
                CREATE TABLE empleado (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(50) NOT NULL,
                CARGO VARCHAR(50) NOT NULL,
                SALARIO INT NOT NULL)
                '''
    
    deleteTable = "DROP TABLE empleado"

    insert = "INSERT INTO empleado VALUES(NULL, ?, ?, ?)"

    select = "SELECT * FROM empleado"

    update = "UPDATE empleado SET NOMBRE =?, CARGO=?, SALARIO=? WHERE ID ="

    delete = "DELETE FROM empleado WHERE ID="

    search = "SELECT * FROM empleado WHERE NOMBRE LIKE '%' || ? || '%' "
