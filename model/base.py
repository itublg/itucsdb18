from abc import ABC, abstractmethod
import logging
import os
import psycopg2 as dbapi2


class Base(ABC):
    def __init__(self):
        self.connection_url = os.getenv("DATABASE_URL")
        #self.connection_url = "postgres://postgres:docker@localhost:5432/postgres"


    @abstractmethod
    def create(self,*args,**kwargs):
        pass

    @abstractmethod
    def insert(self,*args,**kwargs):
        pass
    @abstractmethod
    def update(self,*args,**kwargs):
        pass

    @abstractmethod
    def delete(self, *args, **kwargs):

        pass

    @abstractmethod
    def read(self, *args, **kwargs):

        pass
    def drop(self):
        """
        drop table with given name
        """
        command = """
            drop table {}
        """.format(self.table_name)
        self.execute(command)
    def execute(self, query):

        res = None
        if self.connection_url is None:
            return None
        with dbapi2.connect(self.connection_url) as connection:
            cursor = connection.cursor()
            try:
                cursor.execute(query)
                res = cursor.fetchall()
                cursor.close()
            except dbapi2.Error as e:
                print(f"Query was \n {query} \n error{str(e)}")
                cursor.close()
        return None if res is not None and len(res) == 0 else res

