#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table(
            'place_amenity',
            Base.metadata,
            Column('place_id', String(60), ForeignKey('places.id'),
                   nullable=False, primary_key=True),
            Column('amenity_id', String(60), ForeignKey('amenities.id'),
                   nullable=False, primary_key=True)
            )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    amenity_ids = []
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False,)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)

        reviews = relationship('Review', cascade='delete', backref='place')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0

        @property
        def reviews(self):
            """Getter method to retrieve reviews from FileStorage"""
            from models import storage
            from models.review import Review
            reviews_list = []
            reviews_dict = storage.all(Review)
            for obj in reviews_dict.values():
                if obj.place_id == self.id:
                    reviews_list.append(obj)
            return (reviews_list)

        @property
        def amenities(self):
            """Getter method for amenities in FileStorage"""
            from models import storage
            from models.amenity import Amenity
            amenities_dict = storage.all(Amenity)
            amenity_list = []
            for amenity in amenities_dict.values():
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            """Setter for amenities"""
            from models.amenity import Amenity
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
