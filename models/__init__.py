#!/usr/bin/python3
"""This module instantiates an object of class depending on the value of HBNB_TYPE_STORAGE"""
import os

storage = None
if(os.getenv('HBNB_TYPE_STORAGE') == 'db'):
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

if(storage):
    storage.reload()