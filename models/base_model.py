#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        if not kwargs:
            from models import storage
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if kwargs.get("updated_at"):
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                         '%Y-%m-%dT%H:%M:%S.%f'
                                                         )
            else:
                kwargs['updated_at'] = datetime.now()
            if kwargs.get("created_at"):
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                         '%Y-%m-%dT%H:%M:%S.%f'
                                                         )
            else:
                kwargs['created_at'] = datetime.now()
            # if '__class__' in kwargs.keys():
            #    del kwargs['__class__']
            # self.__dict__.update(kwargs)
            # OR
            for key, value in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        dict_copy = dict(self.__dict__)
        if '_sa_instance_state' in dict_copy.keys():
            del dict_copy['_sa_instance_state']
        return '[{}] ({}) {}'.format(cls, self.id, dict_copy)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        from models import storage
        storage.delete(self)
