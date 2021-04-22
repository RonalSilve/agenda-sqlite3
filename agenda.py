import sqlite3


class Agenda:
    """
    this class contains the attributes and methods of an agenda.
    """
    def __init__(self):
        """
        opening registry and confirming that exists,
        if don't exists build the columns.
        """
        conn = sqlite3.connect('Agenda.db')
        with conn as self.c:
            self.c.execute("""CREATE TABLE IF NOT EXISTS CONTACTOS(
                           Id INTEGER PRIMARY KEY AUTOINCREMENT,
                           Nombre VARCHAR(20), Apellido VARCHAR(20),
                           Edad INTEGER, Telefono VARCHAR(16),
                           Email VARCHAR(20))""")

    def agregar_contacto(self, nombre, apellido, edad, tel, email):
        self.c.execute("INSERT INTO CONTACTOS(NOMBRE,APELLIDO,EDAD,TELEFONO,EMAIL) VALUES ('%s','%s','%s','%s','%s')" % (nombre, apellido,edad, tel, email))
        self.c.commit()

    def listar(self):
        rows = self.c.execute("SELECT *FROM CONTACTOS")
        result = [row for row in rows]
        return result

    def buscar(self, filtrar, mod):
        self.filtrar = filtrar
        self.mod = mod
        self.condition = self.mod+"="+"'"+self.filtrar+"'"
        rows = self.c.execute("""SELECT *FROM CONTACTOS
                             WHERE """+self.condition)
        
        result = [row for row in rows]
        
        return result

    def edit(self, index, change):
        setter = self.mod+"="+"'"+change+"'"
        """
        we locate the index and we take the variable mod
        that represents the attribute to modify
        that was used in search and with 'change'
        we change the value of the attribute
        """
        self.c.execute("UPDATE CONTACTOS SET "+setter +
                       "WHERE Id="+str(index)+" AND " +
                       self.condition)
        self.c.commit()
