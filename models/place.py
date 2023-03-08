#!/usr/bin/python3
"""This module defines a class Place"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.review import Review


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))

class Place(BaseModel, Base):
    """This class defines a place by various attributes"""
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    
    storageType = getenv("HBNB_TYPE_STORAGE")
    if storageType == "db":
        reviews = relationship('Review',
                               cascade="all, delete, delete-orphan",
                               backref="place")
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 back_populates='place_amenities',
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """reviews storage type"""
            from models import storage
            rev = []
            for x in storage.all(Review).values():
                if x.place_id == self.id:
                    rev.append(x)
            return rev

        @property
        def amenities(self):
            """getter"""
            from models import storage
            from models.amenity import Amenity
            ame = []
            moby = storage.all(Amenity)

            for amenity_inst in moby.values():
                if amenity_inst.id == self.amenity_id:
                    ame.append(amenity_inst)
            return ame

        @amenities.setter
        def amenities(self, amenity_list):
            """setter"""
            from models.amenity import Amenity
            for x in amenity_list:
                if type(x) == Amenity:
                    self.amenity_ids.append(x)