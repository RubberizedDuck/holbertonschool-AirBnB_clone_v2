#!/usr/bin/python3
'''Module contains the engine for the db storage.'''

from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.user import User
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage():
    '''Attributes will get system info to start engine.'''
    __engine = None
    __session = None

    def __init__(self):
        '''Creates the engine for SQLALCHEMY.'''
        dialect = 'mysql'
        driver = 'mysqldb'
        sql_user = getenv('HBNB_MYSQL_USER')
        sql_pass = getenv('HBNB_MYSQL_PWD')
        sql_host = getenv('HBNB_MYSQL_HOST')
        sql_db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            f"mysql+mysqldb://{sql_user}:{sql_pass}@{sql_host}/{sql_db}",
            pool_pre_ping=True
        )

        # Drop all tables is test_user for QOL.
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''
        Queries the Database, depending on the object passed through.
        if cls=None, queries all types of objects & returns as dict similar to
        Filestorage.
        key = <class-name>.<object-id>
        value = obj.
        '''
        obj_dict = {}
        class_dict = {
            'State': State, 'City': City, 'User': User,
            'Place': Place, 'Review': Review
        }
        delete = []
        '''Add classes that aren't == cls and delete from class_dict'''
        if cls is not None:
            for k, v in class_dict.items():
                if k != cls:
                    delete.append(k)

            for k in delete:
                del class_dict[k]

        for cls in class_dict:
            query = self.__session.query(class_dict[cls]).all()
            for row in query:
                id = row.id
                key = f'{row.__class__.__name__}.{id}'
                delattr(row, '_sa_instance_state')
                obj_dict[key] = row
        return obj_dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session().delete(obj)

    def reload(self):
        from models.review import Review
        from models.amenity import Amenity
        from models.city import City
        from models.state import State
        from models.place import Place
        from models.user import User
        from models.base_model import BaseModel, Base

        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """ closes the session """
        self.__session.close()
