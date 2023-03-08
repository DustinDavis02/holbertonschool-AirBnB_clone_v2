#!/usr/bin/python3
"""This is the base model class for AirBnB"""
import uuid
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime


Base = declarative_base()


class BaseModel:
    """This class will defines all common attributes/methods
    for other classes
    """
    id = Column("id", String(60), primary_key=True, nullable=False)
    created_at = Column("created_at", DateTime,
                        default=datetime.utcnow(), nullable=False)
    updated_at = Column("updated_at", DateTime,
                        default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiation of base model class
        Args:
            args: it won't be used
            kwargs: arguments for the constructor of the BaseModel
        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date
        """
        if kwargs:
            if 'id' not in kwargs:
                setattr(self, "id", str(uuid.uuid4()))
            if 'created_at' not in kwargs:
                setattr(self, "created_at", datetime.now())
            if 'updated_at' not in kwargs:
                setattr(self, "updated_at", datetime.now())
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """returns a string
        Return:
            returns a string of class name, id, and dictionary
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """return a string representaion
        """
        return self.__str__()

    def save(self):
        """updates the public instance attribute updated_at to current
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """creates dictionary of the class  and returns
        Return:
            returns a dictionary of all the key values in __dict__
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        try:
            del my_dict["_sa_instance_state"]
        except KeyError:
            pass
        return my_dict

    def delete(self):
        """
        Delete A instance of a class
        """
        models.storage.delete(self)