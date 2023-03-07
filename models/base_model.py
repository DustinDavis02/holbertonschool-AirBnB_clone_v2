#!/usr/bin/python3
"""This module defines a class BaseModel to manage file storage for hbnb clone"""

import uuid
from datetime import datetime
from models import storage
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """This class defines all common attributes/methods for other classes"""
    id = Column(String(60), primary_key=True, nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """This method initializes a new instance of the BaseModel class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        for key, value in kwargs.items():
            setattr(self, key, value)
        if 'id' not in kwargs:
            setattr(self, 'id', self.id)
        if 'created_at' not in kwargs:
            setattr(self, 'created_at', self.created_at)
        if 'updated_at' not in kwargs:
            setattr(self, 'updated_at', self.updated_at)

    def __str__(self):
        """Returns a string representation of the BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """This method updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """This method returns a dictionary containing all keys/values of the
        instance and the class name"""
        new_dict = self.__dict__.copy()
        if '_sa_instance_state' in new_dict:
            del new_dict['_sa_instance_state']
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict

    def delete(self):
        """This method deletes the current instance from the storage"""
        storage.delete(self)

