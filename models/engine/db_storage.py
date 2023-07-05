#!/usr/bin/python3
"""db_storage module engine"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import sessionmaker, Session
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.review import Review
from models.place import Place
from models.base_model import BaseModel, Base
import os


class DBStorage:
    """DBStorage class engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Class initializer"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db))
        # Base.metadata.create_all(self.__engine)
        # Session = sesssionmaker(bind=self.__engine)
        # self.__session = Session()
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Method to return all objs of a certain cls"""
        classes = [User, State, City, Amenity, Place, Review]
        dictionary = {}
        if cls is None:
            for class_def in classes:
                results = self.__session.query(class_def).all()
                for obj in results:
                    key = class_def.__name__ + '.' + obj.id
                    value = obj
                    dictionary[key] = value
        else:
            results = self.__session.query(cls)
            for obj in results:
                key = cls.__name__ + '.' + obj.id
                value = obj
                dictionary[key] = value
        return dictionary

    def new(self, obj):
        """Add a new obj to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all the changes made in the current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            ...

    def reload(self):
        """Creates all the tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """close method"""
        self.__session.close()
