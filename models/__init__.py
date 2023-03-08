#!/usr/bin/python3
"""This module instantiates an object of class depending on the value of HBNB_TYPE_STORAGE"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
