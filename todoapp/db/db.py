from .table import Table
from .storage import Storage





class DB:
    def __init__(self,storage):
        """
        Intialiaze database with appropriate table
        """
        self._storage = storage
        self._tables = {}
    
    def table(self,name):
        """ 
        Get acess to a specific named table 
        return a table if exits
        creates a new table if not exist

        """

        if name in self._tables:
            return _tables[name]

        return Table(name,self._storage)

    def drop(self,name):

        if name in self._tables:
            #delete data in table
            _tables[name].truncate()
            del _tables[name]
        
        else:
            raise ValueError("No such table {name}")
    

    def clean(self):
        self._storage.write({})
        self._tables.clear()
    
    
 
        


