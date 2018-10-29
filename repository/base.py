from abc import ABC, abstractmethod
import logging
import os
import psycopg2 as dbapi2


class Base(ABC):
    def __init__(self):
        self.connection_url = os.getenv("DATABASE_URL")
        self.logger = logging.getLogger()

    @abstractmethod
    def create(self, *args, **kwargs):
        pass

    @abstractmethod
    def insert(self, *args, **kwargs):
        pass

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete(self, *args, **kwargs):
        pass

    @abstractmethod
    def read(self, *args, **kwargs):
        pass

    def execute(self, query):
        res = None
        with dbapi2.connect(self.connection_url) as connection:
            cursor = connection.cursor()
            try:
                print(query)
                cursor.execute(query)
                res = cursor.fetchall()
                print(res)
                cursor.close()
            except dbapi2.Error as e:
                self.logger.error(e)
                cursor.close()
        return None if res is not None and  len(res) == 0 else res
