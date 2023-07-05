#!/usr/bin/python3
""" State Module for HBNB project """
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state')

    if getenv('HBNB_TYPE_STORAGE') != "db":
        name = ""
        cities = ""

        @property
        def cities(self):
            from models import storage
            city_dict = storage.all(City)
            # method 1
            # city_instances = [
            #        for key, city_obj in city_dict.items()
            # if city_obj.state_id == self.id
            #        ]
            city_instances = []
            for key, city_obj in city_dict.items():
                if city_obj.state_id == self.id:
                    city_instances.append(city_obj)
            return city_instances
