from todoapp.db import Query,Document



class Table:
    def __init__(self,name:str,storage):
        self._storage=storage
        self._name=name
        table=self._read_table()
        self._next_id=len(table)+1
       

    @property
    def name(self):
        return self._name
    
    def _read_table(self):
        db=self._storage.read()
        db.get(self._name,{})
    
    def _get_next_id(self):
        #table is fresh or it exits
        t=self._next_id
        self._next_id+=1
        return str(t)

    def _update_table(self,updater):
        #get the db
        db=self._storage.read()
        #get the table
        table=db.get(self._name,{})
        #update the table
        table=updater(table)
        #update the db
        db[self._name]=table
        self._storage.write(db)


    def insert(self,data:dict)-> str:
        doc_id=self._get_next_id()
        def updater(table):
            table[doc_id]=Document(doc_id,data)
            return table
        self._update_table(updater)
        return doc_id


       

    def insert_multiple(self,data:list)->list:
        doc_ids=[]
        def updater(table):
            for d in data:
                doc_id=self._get_next_id()
                table[doc_id]=Document(doc_id,d)
                doc_ids.append(doc_id)
        self._update_table(updater)
        return doc_ids



    def update(self,fields:dict,documents:str|Query):
        pass 

    def delete(self,documents:str|Query):
        pass
    
    def get(self,doc_id:str):
        table= self._read_table()
        if doc_id in table:
            return table[doc_id]
        else:
            raise ValueError(f"No such a record with id:{doc_id}")
    def search(self,cond:Query):
        pass









